#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 22:54
# @Email    : yangtianyu92@126.com
from filiter_infomation.template_filiter import template

re_temp = '<div id="main">(.*?)<!-- end: main -->'
website = "加拿大食品检验局网站"


if __name__ == '__main__':
    template(re_temp=re_temp, website=website)