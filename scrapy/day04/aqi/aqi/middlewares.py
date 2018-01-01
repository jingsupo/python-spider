# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
import scrapy


class SeleniumMiddleware(object):
    def process_request(self, request, spider):
        # 通过url地址来判断是否是动态请求
        if 'daydata' in request.url:

            driver = webdriver.Chrome()

            driver.get(request.url)
            html = driver.page_source

            # 直接返回一个Response对象给引擎，引擎会把这个当作下载器返回的响应返回给Spider进行解析处理
            # 表示该请求不再通过下载器下载，而是通过Chrome渲染后再返回
            return scrapy.http.HtmlResponse(url=request.url,
                                     body=html.encode('utf-8'),
                                     encoding='utf-8',
                                     request=request)
