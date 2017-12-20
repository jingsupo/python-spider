#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from  lxml import etree


if __name__ == '__main__':
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a> 
         </ul>
     </div>
    '''

    # 1.转换成 lxml文档
    html_data = etree.HTML(text)

    # 2. 格式化 了解
    html_result = etree.tostring(html_data)
    # print  html_result

    # 3.掌握 xpath
    # 3.1取出所有的li标签
    result = html_data.xpath('//li')
    # 3.2获取所有a标签
    result = html_data.xpath('//li/a')

    # 3.3 取出内容
    result = html_data.xpath('//li/a/text()')

    # 3.4 取出属性的值
    result = html_data.xpath('//li[@class="item-inactive"]/a/@href')

    # 3.5 模糊查询 contains
    result = html_data.xpath('//li[contains(@class,"1")]')

    print result
