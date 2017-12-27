# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from tencent.items import TencentItem, PositionItem
from datetime import datetime


class TencentPipeline(object):
    def open_spider(self, spider):
        self.file_name = open('tencent.json', 'w')

    def process_item(self, item, spider):
        item['source'] = spider.name
        item['crawl_time'] = str(datetime.utcnow())

        if isinstance(item, TencentItem):
            content = json.dumps(dict(item)) + ',\n'
            self.file_name.write(content)
        return item

    def close_spider(self, spider):
        self.file_name.close()


class PositionPipeline(object):
    def open_spider(self, spider):
        self.file_name = open('position.json', 'w')

    def process_item(self, item, spider):
        if isinstance(item, PositionItem):
            content = json.dumps(dict(item)) + ',\n'
            self.file_name.write(content)
        return item

    def close_spider(self, spider):
        self.file_name.close()
