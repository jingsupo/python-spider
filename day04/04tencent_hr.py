# -*- coding:utf-8 -*-

import requests, json, time
from bs4 import BeautifulSoup


class tencent_hr(object):
    def __init__(self):
        self.base_url = "http://hr.tencent.com/position.php?"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.item_list = []
        self.page = 0

    # 发送请求
    def send_request(self, url, params={}):
        time.sleep(2)
        try:
            response = requests.get(url, params=params, headers=self.headers)
            return response.content
        except Exception as e:
            print e

    # 解析数据
    def parse_data(self, data):
        # 初始化
        bs = BeautifulSoup(data, 'lxml')

        # 获取标签-结果为列表
        data_list = bs.select('.even, .odd')

        # 将结果中的每一行数据提取出来
        for data in data_list:
            data_dict = {}
            data_dict['work_name'] = data.select('td a')[0].get_text()
            data_dict['work_type'] = data.select('td')[1].get_text()
            data_dict['work_count'] = data.select('td')[2].get_text()
            data_dict['work_place'] = data.select('td')[3].get_text()
            data_dict['work_time'] = data.select('td')[4].get_text()

            # 将每条字典数据添加进列表
            self.item_list.append(data_dict)

        # 判断是否是最后一页，条件：是否有noactive值
        # 先找到下一页的标签
        next_label = bs.select('#next')
        # 根据标签获取属性class的值-返回结果为列表
        judge = next_label[0].get('class')

        return judge

    # 写入文件
    def write_file(self):
        # 将列表转换成字符串
        data_str = json.dumps(self.item_list)

        with open('04tencent_hr.json', 'w') as f:
            f.write(data_str)

    # 调度运行
    def run(self):
        while True:
            # 拼接参数
            params = {
                "keywords": "python",
                "tid": "0",
                "lid": "2156",
                "start": self.page,
            }

            # 发送请求
            data = self.send_request(self.base_url, params=params)

            # 解析数据
            judge = self.parse_data(data)

            self.page += 10
            print self.page

            # 如果到了最后一页，出现noactive，跳出循环
            if judge:
                break

        self.write_file()


if __name__ == '__main__':
    spider = tencent_hr()
    spider.run()
