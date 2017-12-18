# -*- coding:utf-8 -*-

import urllib2


def web_auth_openner():
    url = "http://60.205.187.28/1.php"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 创建密码管理器
    pwd_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()

    # 添加用户名和密码
    pwd_manager.add_password(realm=None, uri=url, user='admin', passwd='admin')

    # 创建具有web auth认证的管理器
    web_auth_handler = urllib2.HTTPBasicAuthHandler(pwd_manager)

    openner = urllib2.build_opener(web_auth_handler)

    request = urllib2.Request(url, headers=headers)

    response = openner.open(request)

    print response.read()


if __name__ == '__main__':
    web_auth_openner()

