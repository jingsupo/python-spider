# -*- coding:utf-8 -*-

import urllib2

def load_url_data():
    url = 'http://jingsupo.com'

    response = urllib2.urlopen(url)

    data = response.read()

    print data

if __name__ == '__main__':
    load_url_data()
