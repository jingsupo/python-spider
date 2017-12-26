# -*- coding:utf-8 -*-

from selenium import webdriver


def douban_login():
    # 创建浏览器对象
    wd = webdriver.PhantomJS()

    # 发送请求
    wd.get("https://www.douban.com/accounts/login?source=movie")
    wd.save_screenshot('02douban_code.png')
    # code = raw_input('请输入验证码：')

    # 填写用户名 密码 验证码
    wd.find_element_by_name('form_email').send_keys(u'xxx')
    wd.find_element_by_name('form_password').send_keys(u'xxx')
    # wd.find_element_by_id('captcha_field').send_keys(code)

    # 点击登录按钮
    wd.find_element_by_class_name('btn-submit').click()

    # 是否登录成功
    wd.save_screenshot('02logged_in.png')


if __name__ == '__main__':
    douban_login()

