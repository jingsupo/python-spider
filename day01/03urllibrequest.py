# -*- coding:utf-8 -*-

import urllib.request


def load_url_data():
    url = 'http://jingsupo.com'

    response = urllib.request.urlopen(url)

    data = response.read()  # 在python3环境下，读取内容为bytes格式，需要解码

    return data

def write_data(data):
    with open('03.html', 'w') as f:
        f.write(data)

if __name__ == '__main__':
    data = load_url_data().decode()
    write_data(data)
