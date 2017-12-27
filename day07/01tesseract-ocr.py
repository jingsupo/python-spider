# -*- coding:utf-8 -*-

import pytesseract
from PIL import Image


def ocr_image():
    # 加载图片
    # img = Image.open('test.jpg')
    img = Image.open('排序算法.png')

    # 识别
    # txt = pytesseract.image_to_string(img)
    txt = pytesseract.image_to_string(img, lang='chi_sim')

    print txt


if __name__ == '__main__':
    ocr_image()
