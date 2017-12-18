# -*- coding:utf-8 -*-

import urllib2


class Doubanspider(object):
    def __init__(self):
        self.base_url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_request(self):
        try:
            request = urllib2.Request(self.base_url, headers=self.headers)
            response = urllib2.urlopen(request)
            if response.code == 200:
                return response.read()
        except Exception as e:
            print e

    def write_file(self, data):
        with open('01doubanrank.html', 'w') as f:
            f.write(data)


if __name__ == '__main__':
    spider = Doubanspider()
    data = spider.send_request()
    spider.write_file(data)

