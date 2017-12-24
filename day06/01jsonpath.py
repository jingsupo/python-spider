# -*- coding:utf-8 -*-

import requests
from jsonpath import *


def jsonpath_base_use():
    url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 发送请求
    # 注意：只有返回是json文件才可以使用json()方法
    data = requests.get(url, headers=headers).json()

    # 解析-返回结果为列表
    parse_name = jsonpath(data, '$..name')

    for name in parse_name:
        print name


if __name__ == '__main__':
    jsonpath_base_use()
