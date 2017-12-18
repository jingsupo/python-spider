# -*- coding:utf-8 -*-

import urllib2, urllib, cookielib


def send_request():

    # 创建cookjar,用来保存cookie
    cookjar = cookielib.CookieJar()

    # 创建cookie处理器
    cook_handler = urllib2.HTTPCookieProcessor(cookiejar=cookjar)

    cook_openner = urllib2.build_opener(cook_handler)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 需要先登录成功才能获得cookie
    login_url = "http://renren.com/PLogin.do"

    formdata = {
        "email": "mr_mao_hacker@163.com",
        "password": "alarmchime"
    }

    formdata_str = urllib.urlencode(formdata)

    request = urllib2.Request(login_url, data=formdata_str, headers=headers)

    # 发送登录请求，获取cookie
    cook_openner.open(request)

    # 使用包含登录成功cookie的openner发送数据请求

    data_url = "http://www.renren.com/410043129/profile"

    data_request = urllib2.Request(data_url, headers=headers)

    response = cook_openner.open(data_request)

    return response.read()


def write_file(data):
    with open('09cookieopenner.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    data = send_request()
    write_file(data)
