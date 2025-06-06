


          
我需要先了解这个项目的结构和内容，然后生成一个全面的项目总结markdown文件。
        
            
toolName: view_files
            
status: success
          
            
filePath: /Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/README.md
          
继续查看README.md的完整内容，了解项目的详细信息。
        
            
toolName: view_files
            
status: success
          
            
filePath: /Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/README.md
          
查看项目的核心配置文件和脚本，了解项目的技术架构。
        
            
toolName: view_files
            
status: success
          
            
filePath: /Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/pyproject.toml
/Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/run.sh
          
查看GitHub Actions工作流配置和AI增强模块的核心代码。
        
            
toolName: view_files
            
status: success
          
            
filePath: /Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/.github/workflows/run.yml
/Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/ai/enhance.py
          
查看AI增强模块的完整代码和数据结构定义。
        
            
toolName: view_files
            
status: success
          
            
filePath: /Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/ai/enhance.py
/Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/ai/structure.py
          
查看爬虫配置和模板文件，了解数据处理流程。
        
            
toolName: view_files
            
status: success
          
            
filePath: /Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/daily_arxiv/daily_arxiv/spiders
/Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/ai/template.txt
          
查看爬虫目录结构，了解具体的爬虫实现。
        
            
toolName: view_folder
            
status: success
          
/Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/daily_arxiv/daily_arxiv/spiders
          
查看爬虫的具体实现和系统提示词。
        
            
toolName: view_files
            
status: success
          
            
filePath: /Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/daily_arxiv/daily_arxiv/spiders/arxiv.py
/Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/ai/system.txt
          
查看数据转换和README更新脚本，了解完整的数据处理流程。
        
            
toolName: view_files
            
status: success
          
            
filePath: /Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/update_readme.py
/Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/template.md
          
查看to_md目录的内容，了解数据转换为markdown的过程。
        
            
toolName: view_folder
            
status: success
          
/Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/to_md
          
查看数据转换脚本和论文模板，完善对项目的理解。
        
            
toolName: view_files
            
status: success
          
            
filePath: /Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/to_md/convert.py
/Users/mingyang/Documents/daily-arXiv-ai-enhanced/daily-arXiv-ai-enhanced/to_md/paper_template.md
          
# Daily arXiv AI Enhanced 项目总结

## 项目概述

**Daily arXiv AI Enhanced** 是一个自动化的学术论文摘要工具，它每日爬取 arXiv 上的最新论文并使用大语言模型（LLM）生成结构化的中文摘要。该项目通过 GitHub Actions 实现完全自动化的工作流程，为研究人员提供便捷的论文跟踪服务。

## 核心功能

### 1. 自动化论文爬取
- **目标网站**: https://arxiv.org
- **默认类别**: cs.CV（计算机视觉）、cs.GR（计算机图形学）、cs.CL（计算语言学）
- **爬取频率**: 每日自动执行（UTC时间16:30）
- **技术实现**: 基于 Scrapy 框架的网络爬虫

### 2. AI 增强摘要生成
- **默认模型**: DeepSeek Chat
- **输出语言**: 中文（可配置）
- **摘要结构**: 
  - **TL;DR**: 简短总结
  - **Motivation**: 研究动机
  - **Method**: 研究方法
  - **Result**: 研究结果
  - **Conclusion**: 结论

### 3. 自动化内容发布
- **输出格式**: Markdown 文件
- **组织方式**: 按日期和学科分类
- **自动更新**: README.md 自动生成内容索引

## 技术架构

### 项目结构
```
daily-arXiv-ai-enhanced/
├── .github/workflows/run.yml    # GitHub Actions 工作流
├── daily_arxiv/                 # Scrapy 爬虫项目
│   └── spiders/arxiv.py        # arXiv 爬虫实现
├── ai/                         # AI 增强模块
│   ├── enhance.py              # 主要处理脚本
│   ├── structure.py            # 数据结构定义
│   ├── system.txt              # 系统提示词
│   └── template.txt            # 用户提示词模板
├── to_md/                      # Markdown 转换模块
│   ├── convert.py              # 转换脚本
│   └── paper_template.md       # 论文展示模板
├── data/                       # 数据存储目录
├── run.sh                      # 主执行脚本
└── update_readme.py            # README 更新脚本
```

### 核心依赖
- **Python 3.12+**
- **Scrapy 2.12.0+**: 网络爬虫框架
- **LangChain 0.3.20+**: LLM 集成框架
- **LangChain-OpenAI 0.3.9+**: OpenAI API 集成
- **arXiv 2.1.3+**: arXiv API 客户端

## 工作流程

### 1. 数据爬取阶段
```bash
cd daily_arxiv
scrapy crawl arxiv -o ../data/${today}.jsonl
```
- 爬取指定类别的最新论文
- 提取论文ID、标题、作者、摘要等信息
- 输出为 JSONL 格式

### 2. AI 增强阶段
```bash
cd ../ai
python enhance.py --data ../data/${today}.jsonl
```
- 使用 LLM 对每篇论文生成结构化摘要
- 支持函数调用确保输出格式一致性
- 错误处理机制保证流程稳定性

### 3. 格式转换阶段
```bash
cd ../to_md
python convert.py --data ../data/${today}_AI_enhanced_${LANGUAGE}.jsonl
```
- 将 JSONL 数据转换为 Markdown 格式
- 按学科分类组织内容
- 生成目录和导航链接

### 4. 内容发布阶段
```bash
python update_readme.py
```
- 自动更新 README.md 文件
- 添加新生成内容的链接
- 维护历史记录索引

## 配置说明

### GitHub Secrets（敏感信息）
- `OPENAI_API_KEY`: OpenAI API 密钥
- `OPENAI_BASE_URL`: API 基础URL

### GitHub Variables（公开配置）
- `CATEGORIES`: 爬取类别（如 "cs.CL, cs.CV"）
- `LANGUAGE`: 输出语言（如 "Chinese" 或 "English"）
- `MODEL_NAME`: 使用的模型名称（如 "deepseek-chat"）
- `EMAIL`: Git 提交邮箱
- `NAME`: Git 提交用户名

## 数据处理特点

### 1. 去重机制
- 基于论文ID进行去重
- 确保同一论文不会重复处理

### 2. 错误处理
- LLM 输出解析失败时提供默认错误信息
- 保证工作流程不会因单个论文处理失败而中断

### 3. 分类优先级
- 支持自定义学科分类优先级
- 按用户偏好排序展示内容

## 项目优势

### 1. 完全自动化
- 无需人工干预的端到端流程
- GitHub Actions 提供稳定的执行环境

### 2. 高度可配置
- 支持自定义爬取类别、语言、模型
- 灵活的模板系统

### 3. 结构化输出
- 统一的摘要格式便于快速理解
- Markdown 格式便于阅读和分享

### 4. 历史记录管理
- 完整保存每日数据
- 便于回溯和分析

## 使用统计

根据 `data/` 目录显示，项目已稳定运行数月，累计处理了从 2025年3月18日 到 2025年6月6日 的论文数据，展现了良好的稳定性和实用性。

## 未来规划

- **前端界面**: 计划用 GitHub Pages 替代 Markdown 展示
- **功能扩展**: 可能增加更多学科领域支持
- **用户体验**: 持续优化摘要质量和展示效果

## 总结

Daily arXiv AI Enhanced 是一个设计精良的自动化学术工具，它成功地将网络爬虫、人工智能和自动化部署技术结合，为研究人员提供了高质量的论文摘要服务。项目的模块化设计、完善的错误处理和灵活的配置系统使其具有很好的可维护性和扩展性。
        