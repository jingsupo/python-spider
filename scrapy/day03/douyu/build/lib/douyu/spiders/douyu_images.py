# -*- coding: utf-8 -*-
import scrapy, json
from douyu.items import DouyuItem


class DouyuImagesSpider(scrapy.Spider):
    name = 'douyu_images'
    allowed_domains = ['douyucdn.cn']
    base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']

        if data_list:
            for data in data_list:
                item = DouyuItem()
                item['room_id'] = data['room_id']
                item['img_src'] = data['vertical_src']
                item['nickname'] = data['nickname']
                item['city'] = data['anchor_city']

                # yield scrapy.Request(url=item['img_src'], meta={'img_name': item['nickname']}, callback=self.parse_image)

                yield item

            self.offset += 20
            yield scrapy.Request(url=self.base_url + str(self.offset), callback=self.parse)

    """
    def parse_image(self, response):
        with open(response.meta['img_name'] + '.jpg', 'wb') as f:
            f.write(response.body)
    """
