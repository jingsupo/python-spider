# -*- coding:utf-8 -*-

import urllib2, urllib, json


def translate(keyword):
    url = 'http://fanyi.baidu.com/v2transapi'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    formdata = {
        'from':'en',
        'to':'zh',
        'query':keyword,
        'transtype':'enter',
        'simple_means_flag':'3',
    }

    formdata_str = urllib.urlencode(formdata)

    request = urllib2.Request(url, data=formdata_str, headers=headers)

    response = urllib2.urlopen(request)

    try:
        if response.code == 200:
            data = response.read()
            # 将json字符串转化为python dict对象
            data_dict = json.loads(data)
            print data_dict

            ret = data_dict["trans_result"]["data"][0]["dst"]
            print ret
    except Exception as e:
        print e


if __name__ == '__main__':
    keyword = raw_input('请输入要翻译的单词：')
    translate(keyword)

