# -*- coding:utf-8 -*-

import requests, time, gevent
from lxml import etree
from gevent import monkey
monkey.patch_all()

class DoubanMovie(object):
    def __init__(self):
        self.base_url = "https://movie.douban.com/top250"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 电影总数量
        self.count = 0

    def send_request(self, url):
        time.sleep(2)
        try:
            response = requests.get(url, headers=self.headers)
            data = response.content
            self.parse_data(data)
        except Exception as e:
            print e

    def parse_data(self, data):
        html_data = etree.HTML(data)

        # 电影名字
        name_list = html_data.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')

        for name in name_list:
            print name
            # 每获取一部电影名字电影数量增加1
            self.count += 1

    def run(self):
        start_time = time.time()

        gevent_list = []

        for page in range(0, 225 + 1, 25):
            url = self.base_url + '?start=' + str(page)

            # 创建协程
            gevents = gevent.spawn(self.send_request, url)
            gevent_list.append(gevents)

        # 主线程等待
        gevent.joinall(gevent_list)

        end_time = time.time()

        total_time = end_time - start_time

        print '全部电影%d部' % self.count
        print '总时间%ss' % total_time


if __name__ == '__main__':
    spider = DoubanMovie()
    spider.run()
