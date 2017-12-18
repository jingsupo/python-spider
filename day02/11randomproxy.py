# -*- coding:utf-8 -*-

import urllib2


URLErrorCode = 666

def can_use_proxy(request, openner, URLERRORCODE):
    try:
        response = openner.open(request, timeout=3)
        return response.code
    except urllib2.HTTPError as e:
        return e.code
    except urllib2.URLError as e:
        print e
        return URLERRORCODE


if __name__ == '__main__':
    # 大量免费proxy
    proxy_list = [
        {"https":"117.69.142.196:808"},
        {"http":"101.68.73.54:53281"},
        {"http": "113.87.161.227:8118"},
        {"http": "114.245.149.215:8118"},
        {"http": "195.5.40.109:3128"}
    ]

    # 验证有几个能用
    for proxy in proxy_list:
        url = 'http://jingsupo.com'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        request = urllib2.Request(url, headers=headers)
        # 创建proxy处理器
        proxy_handler = urllib2.ProxyHandler(proxy)

        openner = urllib2.build_opener(proxy_handler)

        code = can_use_proxy(request, openner, URLErrorCode)

        print code
