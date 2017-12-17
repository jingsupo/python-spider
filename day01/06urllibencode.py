# -*- coding:utf-8 -*-

import urllib2, urllib


def search_data(keyword):
    # url = "https://www.baidu.com/s?wd=%s" % keyword

    url = 'https://www.baidu.com/s?'

    params = {
        'wd': keyword
    }

    # 字符串和字典不能直接拼接，需要使用urllib库解码
    params_str = urllib.urlencode(params)
    real_url = url + params_str

    # 构造请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        'Connection': 'keep-alive'
    }

    # 构造请求对象
    request = urllib2.Request(real_url, headers=headers)

    # 返回响应
    response = urllib2.urlopen(request)

    return response.read()


def write_file(data):
    with open('06search.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    keyword = raw_input('请输入搜索关键词：')

    data = search_data(keyword)

    write_file(data)
