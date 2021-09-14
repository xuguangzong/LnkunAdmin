#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : gen_captcha.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 10:44
"""
import random
from PIL import Image
from captcha.image import ImageCaptcha


def gen_captcha():
    """ 生成验证码 """
    image = ImageCaptcha()
    # 获取字符串
    captcha_text = ""
    for i in range(4):
        num = random.randint(0, 9)
        letter = chr(random.randint(97, 122))
        Letter = chr(random.randint(65, 90))
        s = str(random.choice([num, letter, Letter]))
        captcha_text += s

    # 生成图像
    captcha_image = Image.open(image.generate(captcha_text))

    return captcha_text, captcha_image
