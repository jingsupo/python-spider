# -*- coding:utf-8 -*-

import urllib2


def proxy_openner():
    '''
    具有代理IP功能的处理器
    :return:
    '''

    # proxy = {'协议':'IP:port'}
    # 付费的代理 proxy = {"协议": "用户名:密码@IP:port"}
    proxy = {"http":"mr_mao_hacker:sffqry9r@120.27.218.32:16816"}
    # 创建具有proxy功能的处理器
    handler = urllib2.ProxyHandler(proxy)
    openner = urllib2.build_opener(handler)

    url = 'http://jingsupo.com'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(url, headers=headers)

    response = openner.open(request)
    print response.read()


if __name__ == '__main__':
    proxy_openner()

