# 导入必要的库
import os  # 操作系统接口，用于环境变量和文件操作
import json  # JSON 数据处理
import sys  # 系统相关的参数和函数

import dotenv  # 环境变量加载
import argparse  # 命令行参数解析

# 导入 LangChain 相关模块
import langchain_core.exceptions  # LangChain 异常处理
from langchain_openai import ChatOpenAI  # OpenAI 聊天模型接口
from langchain.prompts import (
  ChatPromptTemplate,  # 聊天提示模板
  SystemMessagePromptTemplate,  # 系统消息模板
  HumanMessagePromptTemplate,  # 人类消息模板
)
from structure import Structure  # 导入自定义的数据结构

# 如果存在 .env 文件，则加载环境变量
if os.path.exists('.env'):
    dotenv.load_dotenv()

# 读取模板文件内容
template = open("template.txt", "r").read()  # 人类消息模板内容
system = open("system.txt", "r").read()  # 系统消息模板内容

def parse_args():
    """解析命令行参数
    
    Returns:
        argparse.Namespace: 解析后的命令行参数对象
    """
    parser = argparse.ArgumentParser(description="AI 增强论文摘要处理工具")
    parser.add_argument("--data", type=str, required=True, help="输入的 JSONL 数据文件路径")
    return parser.parse_args()

def main():
    """主函数：处理论文数据并进行 AI 增强
    
    工作流程：
    1. 解析命令行参数
    2. 读取和去重数据
    3. 初始化 AI 模型
    4. 逐个处理论文摘要
    5. 保存增强后的数据
    """
    # 解析命令行参数
    args = parse_args()
    
    # 从环境变量获取配置，如果未设置则使用默认值
    model_name = os.environ.get("MODEL_NAME", 'deepseek-chat')  # AI 模型名称
    language = os.environ.get("LANGUAGE", 'Chinese')  # 输出语言

    # 读取 JSONL 文件中的所有数据
    data = []
    with open(args.data, "r", encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))

    # 数据去重：基于论文 ID 去除重复项
    seen_ids = set()  # 用于记录已见过的论文 ID
    unique_data = []  # 存储去重后的数据
    for item in data:
        if item['id'] not in seen_ids:
            seen_ids.add(item['id'])
            unique_data.append(item)

    data = unique_data  # 使用去重后的数据

    # 输出处理信息到标准错误流
    print('Open:', args.data, file=sys.stderr)

    # 初始化 AI 模型，配置结构化输出
    llm = ChatOpenAI(model=model_name).with_structured_output(Structure, method="function_calling")
    print('Connect to:', model_name, file=sys.stderr)
    
    # 构建提示模板：系统消息 + 人类消息
    prompt_template = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system),  # 系统指令
        HumanMessagePromptTemplate.from_template(template=template)  # 用户输入模板
    ])

    # 创建处理链：提示模板 -> AI 模型
    chain = prompt_template | llm

    # 逐个处理每篇论文
    for idx, d in enumerate(data):
        try:
            # 调用 AI 模型进行结构化分析
            response: Structure = chain.invoke({
                "language": language,  # 指定输出语言
                "content": d['summary']  # 论文摘要内容
            })
            # 将 AI 分析结果添加到数据中
            d['AI'] = response.model_dump()
        except langchain_core.exceptions.OutputParserException as e:
            # 处理解析错误：记录错误并设置默认值
            print(f"{d['id']} has an error: {e}", file=sys.stderr)
            d['AI'] = {
                 "tldr": "Error",  # 简要总结
                 "motivation": "Error",  # 研究动机
                 "method": "Error",  # 研究方法
                 "result": "Error",  # 研究结果
                 "conclusion": "Error"  # 结论
            }
        
        # 将处理后的数据追加到输出文件
        output_filename = args.data.replace('.jsonl', f'_AI_enhanced_{language}.jsonl')
        with open(output_filename, "a", encoding='utf-8') as f:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

        # 显示处理进度
        print(f"Finished {idx+1}/{len(data)}", file=sys.stderr)

# 程序入口点
if __name__ == "__main__":
    main()
