# -*- coding:utf-8 -*-

import urllib.request


def load_url_data():
    url = 'http://jingsupo.com'

    response = urllib.request.urlopen(url)

    data = response.read()  # 在python3环境下，读取内容为bytes格式，需要解码

    print(type(data))

    print(data.decode())

if __name__ == '__main__':
    load_url_data()
