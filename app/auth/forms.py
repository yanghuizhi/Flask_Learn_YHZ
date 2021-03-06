# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/1/21 6:58 PM


from flask_wtf import FlaskForm  # 导入基类
# Flask-WTF插件本身不提供字段类型，因此直接从WTForms包中导入了四个表示表单字段的类
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User


class LoginForm(FlaskForm):  # 用户登录表单
    username = StringField(_l('Username'), validators=[DataRequired()])  # 用户名
    password = PasswordField(_l('Password'), validators=[DataRequired()])  # 密码
    remember_me = BooleanField(_l('Remember Me'))  # 复选框
    submit = SubmitField(_l('Sign In'))  # 提交按钮


class RegistrationForm(FlaskForm):  # 用户注册表单
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])  # 双验证器，确保内容与邮件格式结构匹配
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(_l('Repeat Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Register'))


    # 自定义验证，保证不会同数据库中已存在数据产生冲突
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    # 请求重置密码表单类，要求用户输入注册的电子邮件地址
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    # 输入新的密码
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))
