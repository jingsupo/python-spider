# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/PLogin.do']

    def start_requests(self):
        # 如果重写了start_requests，那么start_urls可有可无
        login_url = 'http://renren.com/PLogin.do'
        yield scrapy.FormRequest(
            url=login_url,
            formdata={
                'email': 'xxx',
                'password': 'xxx'
            },
            callback=self.parse
        )

    def parse(self, response):
        url_list = ['http://www.renren.com/410043129/profile',
                    'http://www.renren.com/429732223/profile']

        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        file_name = response.xpath('//title/text()').extract_first() + '.html'
        with open(file_name, 'w') as f:
            f.write(response.body)
