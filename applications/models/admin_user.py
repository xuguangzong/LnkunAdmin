#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : admin_user.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 14:12
"""
import datetime
from flask_login import UserMixin  # 使用flask_login进行用户的登录和登出管理，需要将我们的User模型继承flask_login的UserMixin
from applications.extensions.init_sqlalchemy import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'admin_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = db.Column(db.String(20), comment='用户名')
    realname = db.Column(db.String(20), comment='真实名字')
    avatar = db.Column(db.String(255), comment='头像', default="/static/admin/admin/images/avatar.jpg")
    remark = db.Column(db.String(255), comment='备注')
    password_hash = db.Column(db.String(128), comment='哈希密码')
    enable = db.Column(db.Integer, default=0, comment='启用')
    dept_id = db.Column(db.Integer, comment='部门id')
    create_at = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='创建时间')
    # 反向获取 backref， secondary 多对多关联第三张表
    # lazy="dynamic"只可以用在一对多和多对多关系中，不可以用在一对一和多对一中
    # select: 就是访问到属性的时候，就会全部加载该属性的数据
    # joined: 对关联的两个表使用联接
    # subquery: 与joined类似，但使用子子查询
    # dynamic: 不加载记录，但提供加载记录的查询，也就是生成query对象
    role = db.relationship('Role', secondary="admin_user_role", backref=db.backref('user'), lazy='dynamic')

    def set_password(self, password):
        # 对密码明文密码加盐，生成加密后的hash字符串
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        # 将密码和hash字符串进行比对，返回true或false
        return check_password_hash(self.password_hash, password)
