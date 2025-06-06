# 导入 Scrapy 框架
import scrapy
# 导入操作系统模块，用于获取环境变量
import os


class ArxivSpider(scrapy.Spider):
    """arXiv 论文爬虫类
    
    该爬虫用于抓取 arXiv 网站上的最新论文信息，
    支持多个学科分类的同时抓取。
    """
    
    def __init__(self, *args, **kwargs):
        """初始化爬虫
        
        从环境变量中读取要抓取的论文分类，
        并生成对应的起始 URL 列表。
        """
        super().__init__(*args, **kwargs)
        
        # 从环境变量获取论文分类，默认为计算机视觉(cs.CV)
        categories = os.environ.get("CATEGORIES", "cs.CV")
        
        # 将分类字符串按逗号分割成列表
        categories = categories.split(",")
        
        # 去除每个分类名称前后的空格
        categories = list(map(str.strip, categories))
        
        # 根据分类生成起始URL列表，每个分类对应一个最新论文页面
        self.start_urls = [
            f"https://arxiv.org/list/{cat}/new" for cat in categories
        ]  # 起始URL（计算机科学领域的最新论文）

    # 爬虫名称，用于标识该爬虫
    name = "arxiv"  # 爬虫名称
    
    # 允许爬取的域名列表，限制爬虫只能访问 arxiv.org
    allowed_domains = ["arxiv.org"]  # 允许爬取的域名

    def parse(self, response):
        """解析响应页面，提取论文信息
        
        Args:
            response: Scrapy 响应对象，包含页面内容
            
        Yields:
            dict: 包含论文 ID 的字典
        """
        # 提取每篇论文的信息
        anchors = []
        
        # 遍历页面中的导航链接，获取锚点编号
        # 这些锚点用于确定哪些是当天的新论文
        for li in response.css("div[id=dlpage] ul li"):
            # 从链接中提取 item 编号
            anchors.append(int(li.css("a::attr(href)").get().split("item")[-1]))

        # 遍历页面中的每篇论文条目
        for paper in response.css("dl dt"):
            # 获取当前论文的 item 编号
            paper_item_num = int(paper.css("a[name^='item']::attr(name)").get().split("item")[-1])
            
            # 如果论文编号大于等于最后一个锚点编号，说明是旧论文，跳过
            if paper_item_num >= anchors[-1]:
                continue

            # 提取论文的 arXiv ID 并返回
            yield {
                "id": paper.css("a[title='Abstract']::attr(href)")
                .get()
                .split("/")[-1],  # 提取论文链接中的 ID 部分
            }
