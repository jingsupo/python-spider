# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

if __name__ == '__main__':
        html = """
            <html><head><title>The Dormouse's story</title></head>
            <body>
            <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
            
            <p class="story">
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                and they lived at the bottom of a well.
            </p>
            
            <p class="story">...</p>
            """

        # 1.转换类型
        soup = BeautifulSoup(html, "lxml")

        # 2.1 find  找一个
        # 标签名字  标签属性
        # print soup.find("a", attrs={"id": "link2"})

        # 2.2 find_all()  全局查找 返回list
        # all_list = soup.find_all("a")
        all_list = soup.find_all(attrs={"id": "link3"})
        for element in all_list:
            print element

        # 2.3 select()  全局查找 返回list  css选择器

        '''
           css常用选择器
           
           标签  p
           类   .类名称
           ID   #id名称
           层级  div a
           并集组 span,strong
           属性  div[class="123"]
        '''
        select_list = soup.select(".story")
        select_list = soup.select("#link1")
        select_list = soup.select("p a")
        select_list = soup.select("p[name='dromouse']")

        # 1.获取标签包裹的内容
        content = select_list[0].get_text()
        print content

        # 2.获取标签的属性
        href = soup.select("a")[0].get("href")
        print  href
