#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re

if __name__ == '__main__':

    #正则 在哪里都是一样
    #每个语言 调用的方法不一致

    # re.match("\d+",str)
    # re.search("",str)
    # re.findall()

    # 1.match 默认从头开始  匹配一次
    # 纯数字的正则 ^\d+$
    match_str = "abc123"
    pattern = re.compile("\d+")

    # 指定开始和结束的位置
    result = pattern.match(match_str, 3, 4)

    # 2.search 默认任意位置开始 匹配一次
    result = pattern.search(match_str, 1, 2)

    # 3.findall 全局 返回的是列表
    all_str = "abdsffsdbfsdsbfdsfb"
    all_pattern = re.compile(r"b")
    result = all_pattern.findall(all_str)

    # 4.finditer 全局 返回迭代对像
    result = all_pattern.finditer(all_str)

    for page in result:
         print page.group()
