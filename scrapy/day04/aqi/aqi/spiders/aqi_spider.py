# -*- coding:utf-8 -*-

import scrapy
from aqi.items import AqiItem


class AqiSpider(scrapy.Spider):
    name = 'aqi_spider'
    allowed_domains = ['aqistudy.cn']

    base_url = 'https://www.aqistudy.cn/historydata/'

    start_urls = [base_url]

    def parse(self, response):
        """
            从response获取每个城市的链接， 并发送请求（383个城市）
        :param response:
        :return:
        """
        link_list = response.xpath('//div[@class="all"]//li/a/@href').extract()
        name_list = response.xpath('//div[@class="all"]//li/a/text()').extract()

        for link, name in zip(link_list, name_list)[10:11]:
            yield scrapy.Request(url=self.base_url + link, meta={'name': name}, callback=self.parse_month)

    def parse_month(self, response):
        """
            从response获取每个城市每个月的链接，并发送请求（每个城市48个月）
        :param response:
        :return:
        """
        link_list = response.xpath('//ul[@class="unstyled1"]//li/a/@href').extract()

        for link in link_list[20:21]:
            print '*'*30
            print self.base_url + link
            yield scrapy.Request(url=self.base_url + link, meta=response.meta, callback=self.parse_day)

    def parse_day(self, response):
        print response.body
        """
            每个城市每一天的数据
        :param response:
        :return:
        """
        tr_list = response.xpath('//div[@class="row"]//tr')
        tr_list.pop(0)
        print '*'*30
        print tr_list

        for tr in tr_list:
            item = AqiItem()
            item['city'] = response.meta['name']
            item['date'] = tr.xpath('./td[1]/text()').extract_first()
            item['aqi'] = tr.xpath('./td[2]/text()').extract_first()
            item['level'] = tr.xpath('./td[3]//text()').extract_first()
            item['pm2_5'] = tr.xpath('./td[4]/text()').extract_first()
            item['pm10'] = tr.xpath('./td[5]/text()').extract_first()
            item['so2'] = tr.xpath('./td[6]/text()').extract_first()
            item['co'] = tr.xpath('./td[7]/text()').extract_first()
            item['no2'] = tr.xpath('./td[8]/text()').extract_first()
            item['o3'] = tr.xpath('./td[9]/text()').extract_first()

            yield item
