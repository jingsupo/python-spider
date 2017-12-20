#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re

if __name__ == '__main__':
    # 1. 点的问题 ; DOTALL re.S
    str = '''
        asfdsfdsffsdb
        ooooooooo
        rrrrrr
        dsfdfssB

    '''
    # pattern = re.compile("a(.*)b",re.S)
    # pattern = re.compile("a(.*)b", re.DOTALL)

    # 即是re.S 又忽略大小写
    pattern = re.compile("a(.*)b", re.DOTALL | re.I)

    result = pattern.findall(str)

    print result

    # 2. r"fsdsfd" 原始的字符串 --> 正则
    # \b 回退一个字节
    str2 = "a\bb"
    print str2