# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from settings import USER_AGENT_LIST
import random


class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = user_agent


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = 'http://username:password@ip:port'
        request.meta['proxy'] = proxy
