# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AqiItem(scrapy.Item):
    # 城市
    city = scrapy.Field()

    date = scrapy.Field()
    aqi = scrapy.Field()
    level = scrapy.Field()
    pm2_5 = scrapy.Field()
    pm10 = scrapy.Field()
    so2 = scrapy.Field()
    co = scrapy.Field()
    no2 = scrapy.Field()
    o3 = scrapy.Field()

    # 抓取时间
    crawl_time = scrapy.Field()
    # 数据源
    source = scrapy.Field()
