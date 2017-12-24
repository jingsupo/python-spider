# -*- coding:utf-8 -*-

import requests, json, jsonpath, urllib, random, time


class LagouSpider(object):
    def __init__(self):
        self.base_url = "https://www.lagou.com/jobs/positionAjax.json"
        self.headers = {
            # "Accept": "application/json, text/javascript, */*; q=0.01",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Accept-Language": "zh-CN,zh;q=0.9",
            # "Connection": "keep-alive",
            # "Content-Length": "23",
            # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            # 反爬字段 1
            "Cookie": "_ga=GA1.2.141982794.1513838184; user_trace_token=20171221143624-43c39b96-e619-11e7-a409-525400f775ce; LGUID=20171221143624-43c39e32-e619-11e7-a409-525400f775ce; _gid=GA1.2.1911809108.1513838184; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAACEBACDG18079CDF31E87E380D301BE8438F20C8; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513838184,1513904123; X_HTTP_TOKEN=d83dd14ec928f4dc04e403c7a7e0d6eb; _gat=1; LGSID=20171222165040-2ff5aea0-e6f5-11e7-9e03-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_navigation; SEARCH_ID=7436bebb4a7d40feb27929f3694161ee; LGRID=20171222165558-ed78c2e0-e6f5-11e7-a52a-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513932959",
            # "Host": "www.lagou.com",
            # "Origin": "https://www.lagou.com",
            # 反爬字段 2
            "Referer": "https://www.lagou.com/jobs/list_PHP?px=default&city=%E4%B8%8A%E6%B5%B7",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            # "X-Anit-Forge-Code": "0",
            # "X-Anit-Forge-Token": "None",
            # "X-Requested-With": "XMLHttpRequest",
        }

        self.city = raw_input('请输入城市名字：')
        self.position = raw_input('请输入搜索职位：')
        # 代理IP列表
        self.proxy_list = [
            {"http": "112.74.32.237:6666"},
            {"http": "113.122.50.147:808"}
        ]
        self.item_list = []
        self.page = 1
        # 是否结束抓取的标志
        self.isworking = True

    def send_request(self):
        time.sleep(1)
        print '正在抓取第%d页' % self.page

        params = {
            "px": "default",
            "city": self.city,
            "needAddtionalResult": "false",
            "isSchoolJob": "0"
        }

        formdata = {
            "first": "false",
            "pn": self.page,
            "kd": self.position
        }

        # 在这里转码 只是为了获取字节长度
        formdata_str = urllib.urlencode(formdata)
        content_length = len(formdata)

        # 随机获取代理IP
        random_proxy = random.choice(self.proxy_list)

        try:
            response = requests.post(self.base_url, data=formdata, params=params, headers=self.headers, proxies=random_proxy)
            return response.json()
        except Exception as e:
            print e

    def parse_data(self, data):
        # 取出职位信息
        result_data = jsonpath.jsonpath(data, '$..result')[0]
        print len(result_data)

        if not len(result_data):
            print '数据爬取结束😂'
            self.isworking = False
            return

        for content in result_data:
            dict = {}
            dict["positionName"] = content["positionName"]
            dict["salary"] = content["salary"]
            dict["education"] = content["education"]
            self.item_list.append(dict)

    def write_file(self):
        json.dump(self.item_list, open('02lagou.json', 'w'))
        print '数据保存成功😄'

    def run(self):
        while self.isworking:
            data = self.send_request()
            self.parse_data(data)
            self.page += 1

        self.write_file()


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
