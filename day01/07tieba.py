# -*- coding:utf-8 -*-

import urllib2, urllib, time


class Tiebaspider(object):
    def __init__(self, tieba_name, start_page, end_page):
        self.base_url = 'https://tieba.baidu.com/f?'
        self.name = tieba_name
        self.start = start_page
        self.end = end_page
        self.headers = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
            'Connection': 'keep-alive'
        }

    # 发送请求
    def send_request(self, url):
        time.sleep(2)

        try:
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            if response.code == 200:
                return response.read()
        except Exception as e:
            print e

    # 下载文件
    def write_data(self, data, page):
        filename = 'tieba/' + str(page) + '页.html'
        print '%s正在下载...' % filename
        with open(filename, 'w') as f:
            f.write(data)

    # 调度方法
    def start_work(self):
        for page in range(self.start, self.end + 1):
            pn = (page - 1) * 50
            params = {
                'kw': self.name,
                'pn': pn
            }

            # 字典转码后与base_url进行拼接
            params_str = urllib.urlencode(params)
            url = self.base_url + params_str

            data = self.send_request(url)
            self.write_data(data, page)

if __name__ == '__main__':
    tie_name = raw_input('请输入贴吧名字：')
    start_page = int(raw_input('开始页：'))
    end_page = int(raw_input('结束页：'))

    spider = Tiebaspider(tie_name, start_page, end_page)

    spider.start_work()
