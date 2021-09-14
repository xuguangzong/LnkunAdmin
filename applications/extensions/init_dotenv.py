#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : init_dotenv.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 15:15
"""

import os
from dotenv import load_dotenv

root_path = os.path.abspath(os.path.dirname(__file__)).split('applications')[0]
dot_env_path = os.path.join(root_path, '.env')
flask_env_path = os.path.join(root_path, '.flaskenv')

if os.path.exists(dot_env_path):
    load_dotenv(dot_env_path)

if os.path.exists(flask_env_path):
    load_dotenv(flask_env_path)
