#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 22:54
# @Email    : yangtianyu92@126.com
from filiter_infomation.template_filiter import template

re_temp = 'name=\'page-body\' >(.*?)<span id="last-modified-text">.*</span>'
website = "美国农业部食品安全检验局"


if __name__ == '__main__':
    template(table="recall2018", re_temp=re_temp, website=website)