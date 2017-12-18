# -*- coding:utf-8 -*-

import urllib2, urllib, time


class Doubanspider(object):
    def __init__(self):
        self.base_url = 'https://movie.douban.com/j/chart/top_list?'
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_request(self, url):
        time.sleep(2)

        try:
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            if response.code == 200:
                return response.read()
        except Exception as e:
            print e
    
    def write_file(self, data):
        with open('02doubanmovielist.html', 'w') as f:
            f.write(data)

    def start_work(self):
        # type=5&interval_id=100%3A90&action=&start=0&limit=20
        
        params = {
            'type': '5',
            'interval_id': '100:90',
            'action': '',
            'start': '0',
            'limit': '2',
        }
    
        url = self.base_url + urllib.urlencode(params)

        data = self.send_request(url)
        self.write_file(data)


if __name__ == '__main__':
    spider = Doubanspider()
    spider.start_work()




