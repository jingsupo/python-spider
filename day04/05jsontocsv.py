# -*- coding:utf-8 -*-

import json, csv

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def json_to_csv():
    # 读取json文件
    json_file = open('04tencent_hr.json', 'r')

    # 创建csv文件
    csv_file = open('05json.csv', 'w')

    # 创建读写器
    csv_writer = csv.writer(csv_file)

    # 提取表头和正文内容
    data = json.load(json_file)

    # 表头
    sheet_title = data[0].keys()

    # 正文内容
    content_list = [dict.values() for dict in data]

    # 通过读写器写入csv文件
    csv_writer.writerow(sheet_title)
    csv_writer.writerows(content_list)

    # 关闭文件
    json_file.close()
    csv_file.close()


if __name__ == '__main__':
    json_to_csv()
