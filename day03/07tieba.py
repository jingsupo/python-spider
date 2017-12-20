#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests, time
from lxml import etree


class Tiebaspider(object):
    def __init__(self, tiebaname, start_page, end_page):
        self.base_url = "http://tieba.baidu.com"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.name = tiebaname
        self.start = start_page
        self.end = end_page

        # 第一层解析 xpath
        self.first_xpath = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        # 第二层解析 xpath
        self.second_xpath = '//img[@class="BDE_Image"]/@src'

    # 发送请求
    def send_request(self, url, params={}):
        time.sleep(1)
        try:
            response = requests.get(url, params=params, headers=self.headers)
            return response.content
        except Exception as e:
            print e

    # 写入文件
    def write_file(self, data, page):
        print page
        filename = 'tieba/' + page
        with open(filename, 'w') as f:
            f.write(data)

    # 解析数据
    def parse_data(self, data, xpath):
        # 转换html类型
        html_data = etree.HTML(data)
        # 解析
        data_list = html_data.xpath(xpath)

        return data_list

    # 调度运行
    def run(self):
        for page in range(self.start, self.end + 1):
            pn = (page - 1) * 50
            params = {
                'kw': self.name,
                'pn': pn
            }

            # 发送第一次请求
            first_response = self.send_request(self.base_url + '/f?', params=params)
            # 解析提取子链接 每一条单独的帖子
            first_data_list = self.parse_data(first_response, self.first_xpath)

            # 请求每条帖子的数据
            for link in first_data_list:
                # 拼接每条帖子的url
                url = self.base_url + link

                # 发送第二次请求
                second_response = self.send_request(url)
                # 解析提取每个帖子里面的图片地址
                second_data_list = self.parse_data(second_response, self.second_xpath)

                # 发送图片请求 保存图片到本地
                for img_url in second_data_list:
                    # 发送请求
                    image_file = self.send_request(img_url)
                    # 截取图片链接后15位作为文件名
                    page = img_url[-15:]
                    # 保存图片
                    self.write_file(image_file, page)


if __name__ == '__main__':
    tiebaname = '美女'
    start_page = 1
    end_page = 1

    spider = Tiebaspider(tiebaname, start_page, end_page)
    spider.run()
