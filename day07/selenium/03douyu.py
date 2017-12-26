# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import time


class DouyuSpider(object):
    def __init__(self):
        self.base_url = "https://www.douyu.com/directory/all"
        # 浏览器对象
        self.driver = webdriver.PhantomJS()
        # 房间总数
        self.count = 0
        # 总页数
        self.page = 1

    def send_request(self):
        self.driver.get(self.base_url)

        # 什么时候结束 class = shark-pager-disable-next 有则结束，没有则继续循环
        while True:
            print '正在下载第%d页' % self.page
            time.sleep(1)
            self.page += 1
            data = self.driver.page_source
            self.parse_data(data)

            # 字符串查找find shark-pager-disable-next
            if data.find('shark-pager-disable-next') != -1:
                break

            # 点击下一页，继续获取数据
            self.driver.find_element_by_class_name('shark-pager-next').click()

    def parse_data(self, data):
        bs = BeautifulSoup(data, 'lxml')

        # 解析
        # 房间名字
        home_list = bs.select('#live-list-content .ellipsis')
        # 主播名字
        name_list = bs.select('#live-list-content .dy-name')
        # 房间人气
        pop_list = bs.select('#live-list-content .dy-num')

        for home, name, pop in zip(home_list, name_list, pop_list):
            print home.get_text().strip()
            print name.get_text()
            print pop.get_text()

            self.count += 1

        print self.count


if __name__ == '__main__':
    spider = DouyuSpider()
    spider.send_request()
