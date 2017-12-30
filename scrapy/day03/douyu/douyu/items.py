# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # 房间ID
    room_id = scrapy.Field()
    # 图片链接
    img_src = scrapy.Field()
    # 主播艺名
    nickname = scrapy.Field()
    # 所在城市
    city = scrapy.Field()
    # 图片保存的路径
    img_path = scrapy.Field()
    # 爬虫源
    source = scrapy.Field()
    # 抓取时间
    crawl_time = scrapy.Field()
