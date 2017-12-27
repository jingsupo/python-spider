# -*- coding:utf-8 -*-

import scrapy
from tencent.items import TencentItem, PositionItem


class TencentSpider(scrapy.Spider):
    # 爬虫名
    name = 'tencent2'
    # 允许爬取的域名列表
    allowed_domains = ['hr.tencent.com']

    base_url = 'http://hr.tencent.com/position.php?&start='
    # url地址的偏移量，每次自增10
    offset = 0
    # 起始url地址列表
    # start_urls = [base_url + str(offset)]
    # 将所有url放入start_urls，实现真正高并发
    start_urls = [base_url + str(num) for num in range(0, 2681, 10)]


    def parse(self, response):
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
            yield scrapy.Request(url=item['position_link'], callback=self.parse_position)

            # 每获取一条职位信息就将item对象提交给引擎，然后转交给管道处理
            yield item

        # 2.通过获取下一页处理多页数据
        """
        # 如果返回None，表示没有到最后一页
        if not response.xpath('//a[@id="next" and @class="noactive"]/@href').extract_first():
            next_link = 'http://hr.tencent.com/' + response.xpath('//a[@id="next"]/@href').extract_first()

            yield scrapy.Request(next_link, callback=self.parse)
        """

        # 1.通过offset偏移量控制url地址
        """
        # 当偏移量达到2680，表示到达最后一页，就不再发送请求
        if self.offset <= 2680:
            self.offset += 10

            yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse)
        """

    def parse_position(self, response):
        item = PositionItem()

        item['position_duty'] = ''.join(response.xpath('//ul[@class="squareli"]')[0].xpath('./li/text()').extract())
        item['position_requirement'] = ''.join(response.xpath('//ul[@class="squareli"]')[0].xpath('./li/text()').extract())

        yield item
