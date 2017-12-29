# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem, PositionItem


class TencentHrSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    # start_urls里的链接请求发送后，仅仅经过每一个Rule提取链接
    start_urls = ['http://hr.tencent.com/position.php?start=0']

    rules = (
        # 每个follow=true的响应，默认都会经过所有的Rule进行链接提取
        # 如果callback有回调函数，默认follow=False
        # 如果callback没有回调函数，默认follow=True

        # 提取列表页的url，并构建请求发送
        Rule(LinkExtractor(allow=r'start='), callback='parse_list', follow=True),
        # 构建详情页的url，并构建请求发送
        Rule(LinkExtractor(allow=r'position_detail\.php\?id='), callback='parse_item'),
    )

    def parse_list(self, response):

        node_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        for node in node_list:
            item = TencentItem()

            item['position_name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['position_link'] = 'http://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract_first()
            item['position_type'] = node.xpath('./td[2]/text()').extract_first()
            item['position_nums'] = node.xpath('./td[3]/text()').extract_first()
            item['work_location'] = node.xpath('./td[4]/text()').extract_first()
            item['publish_times'] = node.xpath('./td[5]/text()').extract_first()

            # 发送每个职位详情页到请求，并指定回调函数处理响应
            yield scrapy.Request(url=item['position_link'], callback=self.parse_item)

            # 每获取一条职位信息就将item对象提交给引擎，然后转交给管道处理
            yield item

    def parse_item(self, response):
        item = PositionItem()

        item['position_duty'] = ''.join(response.xpath('//ul[@class="squareli"]')[0].xpath('./li/text()').extract())
        item['position_requirement'] = ''.join(
            response.xpath('//ul[@class="squareli"]')[0].xpath('./li/text()').extract())

        yield item
