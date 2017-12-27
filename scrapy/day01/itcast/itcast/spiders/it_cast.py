# _*_ coding:utf-8 _*_

import scrapy
from itcast.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    # 爬虫名字
    name = 'itcast'
    # 允许爬取的域名范围
    allowed_domains = ['itcast.cn']
    # 爬虫启动时，发送的第一批url地址列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    """
    def parse(self, response):
    node_list = response.xpath('//div[@class="li_txt"]')
    
    item_list = []
    for node in node_list:
        item = ItcastItem()
        item['name'] = node.xpath('./h3/text()').extract_first()
        item['title'] = node.xpath('./h4/text()').extract_first()
        item['info'] = node.xpath('./p/text()').extract_first()
        item_list.append(item)
    return item_list  # 返回结果集为列表，结合scrapy crawl itcast -o itcast.json/xml/csv可以保存为相应后缀的文件

    """

    def parse(self, response):
        # 获取所有老师信息的节点
        node_list = response.xpath('//div[@class="li_txt"]')
        # 迭代节点列表，获取每个老师的信息
        for node in node_list:
            item = ItcastItem()
            item['name'] = node.xpath('./h3/text()').extract_first()
            item['title'] = node.xpath('./h4/text()').extract_first()
            item['info'] = node.xpath('./p/text()').extract_first()
            yield item
