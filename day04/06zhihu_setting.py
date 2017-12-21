# -*- coding:utf-8 -*-

import requests, time
from bs4 import BeautifulSoup


# 发送请求
def load_setting():
    # 创建session
    session = requests.session()

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    # 获取_xsrf
    url = "https://www.zhihu.com/"
    xsrf_data = session.get(url, headers=headers).content
    xsrf = parse_data(xsrf_data)

    # 发送验证码 获取验证码参数 保存图片
    # https: // www.zhihu.com / captcha.gif?type = login & lang = en & r = + "时间"
    captcha_url = "https://www.zhihu.com/captcha.gif?type=login&lang=en&r=" + str(int(time.time() * 1000))
    captcha_data = session.get(captcha_url, headers=headers).content
    write_file(captcha_data)
    captcha_code = raw_input('请输入验证码：')

    # 发送登录请求
    login_url = "https://www.zhihu.com/login/email"

    form_data = {
        "email": "1019197976@qq.com",
        "password": "l123456",
        "_xsrf": xsrf,
        "captcha": captcha_code,
        "captcha_type": "en"
    }

    session.post(login_url, data=form_data, headers=headers)

    # 发送设置页面的数据请求
    setting_url = "https://www.zhihu.com/settings/profile"
    data = session.get(setting_url, headers=headers).content

    print data


# 解析数据
def parse_data(data):
    bs = BeautifulSoup(data, 'lxml')
    xsrf = bs.select('input[name="_xsrf"]')[0].get('value')
    return xsrf


# 写入文件
def write_file(data):
    with open('06code.png', 'wb') as f:
        f.write(data)
    pass


if __name__ == '__main__':
    load_setting()
