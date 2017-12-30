# -*- coding:utf-8 -*-

from scrapy import cmdline


# 下面两种形式都可以执行
# cmdline.execute(['scrapy', 'genspider', 'baidu', 'baidu.com'])
# cmdline.execute(['scrapy', 'crawl', 'baidu'])
# cmdline.execute('scrapy genspider baidu baidu.com'.split())
# cmdline.execute('scrapy crawl baidu'.split())


# cmdline.execute('scrapy genspider renren renren.com'.split())
cmdline.execute('scrapy crawl renren'.split())
