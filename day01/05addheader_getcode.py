# -*- coding:utf-8 -*-

import urllib2


def load_url_data():
    # url
    url = 'http://www.baidu.com'

    # 构造请求对象
    request = urllib2.Request(url)
    request.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
    request.add_header('Connection', 'keep-alive')

    # 发送请求
    response = urllib2.urlopen(request)

    # 获取请求头-首字母大写，其余小写
    user = request.get_header('User-agent')
    print user

    # 返回数据
    code = response.getcode()
    print code

    # 获取真实的url
    real_url = response.geturl()
    print real_url

    if code == 200:
        return response.read()

if __name__ == '__main__':
    data = load_url_data()
    print data
