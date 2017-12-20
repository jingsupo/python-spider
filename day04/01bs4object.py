# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

if __name__ == '__main__':
    html = """
           <html><head><title>The Dormouse's story</title></head>
           <body>
           <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
           <p class="story">Once upon a time there were three little sisters; and their names were
           <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
           <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
           <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
           and they lived at the bottom of a well.</p>
           <p class="story">...</p>
           """

    # 1.转换对象类型 soup
    soup = BeautifulSoup(html, "lxml")

    # 2. 四大对象

    # 2.1 Tag --> 标签本身只能获取最上面的一个

    print soup.head
    # print type(soup.title)  # <class 'bs4.element.Tag'>

    # 2.2 Navigablestring

    print soup.title.string
    # print type(soup.title.string)  # <class 'bs4.element.NavigableString'>

    # 2.3 BeaufulSoup
    # print type(soup)
    # print soup.name
    print soup.p.attrs

    # 2.4 comment :注释里面的内容

    print soup.a
    print soup.a.string
    # print type(soup.a.string)

    print soup.html.contents
