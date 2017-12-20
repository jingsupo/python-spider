#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests, re, time


class Neihanspider(object):
    def __init__(self):
        self.base_url = 'http://www.neihan8.com/article/list_5_'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 第一层解析的正则表达式 正则里面的符号不能改，必须照原样复制过来
        self.first_pattern = re.compile(r'<div class="f18 mb20">.*?</div>', re.S)
        # 第二层解析的正则表达式 去除所有标签 字符实体 空白 全角空格
        self.second_pattern = re.compile(r'<.*?>|&.*?;|\s|　　')

    # 发送请求
    def send_request(self, url):
        time.sleep(2)
        try:
            response = requests.get(url, headers=self.headers)
            return response.content
        except Exception as e:
            print e

    # 写入文件
    def write_file(self, data, page):
        with open('04neihanba.txt', 'a') as f:
            filename = '第' + str(page) + '页的段子\n'
            print filename
            f.write('-' * 10 + '\n')
            f.write(filename)
            f.write('-' * 10 + '\n')

            for first_data in data:
                # 第二层解析
                content = self.second_pattern.sub('', first_data)
                f.write(content)
                # 在每个段子结束的时候加个换行
                f.write('\n\n')

    # 调度方法
    def start_work(self):
        for page in range(1, 5):
            # 拼接url
            url = self.base_url + str(page) + '.html'

            # 发送请求
            data = self.send_request(url)

            # 转码
            data = data.decode('gbk').encode('utf-8')

            # 第一层解析
            data_list = self.first_pattern.findall(data)

            # 将数据写入文件
            self.write_file(data_list, page)


if __name__ == '__main__':
    spider = Neihanspider()
    spider.start_work()
