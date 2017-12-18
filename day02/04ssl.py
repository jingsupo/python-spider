# -*- coding:utf-8 -*-

import urllib2, ssl


def ssl_load_data():
    url = "https://www.12306.cn/mormhweb/"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    request = urllib2.Request(url, headers=headers)

    context = ssl._create_unverified_context()

    response = urllib2.urlopen(request, context=context)

    data = response.read()

    with open('04ssl.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    ssl_load_data()
