# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy, os
from scrapy.pipelines.images import ImagesPipeline
from settings import IMAGES_STORE
import logging
from pymongo import MongoClient
from datetime import datetime


class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item


class DouyuImagesPipeline(ImagesPipeline):
    # 发送每个图片的请求，并自动保存到settings中IMAGES_STORE指定的路径下
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_src'])

    def item_completed(self, results, item, info):
        # 返回图片原来名字的字符串
        img_path = IMAGES_STORE + [x['path'] for ok, x in results if ok][0]
        new_name = IMAGES_STORE + item['nickname'] + '.jpg'
        item['img_path'] = new_name
        # 更改文件名
        try:
            os.rename(img_path, new_name)
        except Exception as e:
            logging.error('图片已被修改')

        return item


class DouyuMongoPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client.douyu

    def process_item(self, item, spider):
        item['source'] = spider.name
        item['crawl_time'] = str(datetime.utcnow())
        self.db.item.insert(dict(item))

        return item
