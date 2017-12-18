# -*- coding:utf-8 -*-

import urllib2


# 代理IP webauth认证 cookie，这些功能urllib2自带的urlopen做不到
# 需要创建处理器 自定义openner

def custom_openner():
    # 创建处理器
    handler = urllib2.HTTPHandler()

    # 自定义openner
    openner = urllib2.build_opener(handler)

    url = 'http://jingsupo.com'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(url, headers=headers)

    response = openner.open(request)

    print response.read()


if __name__ == '__main__':
    custom_openner()

