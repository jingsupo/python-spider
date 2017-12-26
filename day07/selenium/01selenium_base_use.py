# -*- coding:utf-8 -*-

from selenium import webdriver

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def selenium_base_use():
    # 创建浏览器对象
    driver = webdriver.PhantomJS()

    # 请求数据
    driver.get('http://www.baidu.com')

    # 获取数据
    data = driver.page_source

    with open('01baidu.html', 'w') as f:
        f.write(data)

    # 点击新闻按钮
    driver.find_element_by_name('tj_trnews').click()

    # 在输入框输入数据：Unicode编码
    driver.find_element_by_id('ww').send_keys(u'深度学习')

    # 点击 百度一下 按钮
    driver.find_element_by_class_name('btn').click()

    # 保存截屏
    # driver.save_screenshot('01baidu.png')

    # 点击第一条新闻
    driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()

    # 找到新打开的页面 list
    print driver.window_handles
    print driver.current_url

    # 根据角标可以切换页面
    driver.switch_to.window(driver.window_handles[1])

    # driver.save_screenshot('02baidu.png')

    # 再次回到上一个页面
    driver.switch_to.window(driver.window_handles[0])

    # 获取当前的url
    print driver.current_url

    # 获取所有的cookie
    cookies = driver.get_cookies()
    # print cookies

    print 'over...'

    # 关闭当前页面
    driver.close()

    print driver.window_handles

    # 关闭浏览器
    driver.quit()


if __name__ == '__main__':
    selenium_base_use()
