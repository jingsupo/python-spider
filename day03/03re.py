#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re

if __name__ == '__main__':

    # 1.split  分割字符串
    split_str = "a b,c,;;fsd;;lkfs8,,,,;;d 10"
    split_pattern = re.compile("[,;\s]+")
    result = split_pattern.split(split_str)
    print result
    # 2.sub  替换字符和调换顺序
    sub_str = "hello world,,;;a b;;;fdasfds;c d"
    sub_pattern = re.compile("(\w+) (\w+)")
    # 替换
    result = sub_pattern.sub("#", sub_str)
    print result
    # 调换顺序  分组
    result = sub_pattern.sub(r"\2 \1", sub_str)
    print result
    # 3.汉字 unicode 无论字符还是正则都是unicode
    chi_str = u"小明是好孩子,老王是坏人 is True"
    chi_pattern = re.compile(u"[\u4e00-\u9fa5]+")
    result = chi_pattern.findall(chi_str)

    for name in result:

        print name
