# -*- coding:utf-8 -*-

import urllib2


def send_request():
    # 1.url -- 直接访问的 登录之后的数据
    url = "http://www.renren.com/410043129/profile"

    # 2.headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",

               "Cookie":"anonymid=jbaf8ove-oq15c7; depovince=BJ; _r01_=1; JSESSIONID=abcy_Oaz_iDHJ8WAxrJbw; ick_login=538b4172-9d51-485f-8706-d87db6cf5cc4; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=c5a1a9595705e814c2731870d90930e49; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20171217/1110/main_ubup_a4bf00008c1f1986.jpg; t=08fd5dc28bc0fac27a503d37996a7b639; societyguester=08fd5dc28bc0fac27a503d37996a7b639; id=327550029; xnsid=9cba110b; loginfrom=syshome; ch_id=10016; jebecookies=a9b0653a-2a6e-4d8b-b6f6-e970f5bd8219|||||; wp_fold=0; jebe_key=ea6b28bf-8f3e-4427-8186-ecd0884c387a%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1513502487281%7C1"
               }

    request = urllib2.Request(url, headers=headers)

    response = urllib2.urlopen(request)

    return response.read()


def write_file(data):
    with open('08renren.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    data = send_request()
    write_file(data)
