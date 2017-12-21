# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from lxml import etree


def parse_xsrf():
    url = "https://www.zhihu.com"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求
    response = requests.get(url, headers=headers).content

    # 解析数据
    # 4.1 bs4
    bs = BeautifulSoup(response, 'lxml')  # 指定解析器为lxml

    result = bs.select('input[name="_xsrf"]')  # 获取结果为列表

    xsrf = result[0].get('value')  # 获取value的属性值

    print xsrf

    # 4.2 xpath
    html = etree.HTML(response)

    result = html.xpath('//input[@name="_xsrf"]/@value')  # 结果为列表

    xsrf = result[0]

    print xsrf


if __name__ == '__main__':
    parse_xsrf()
