#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 17:11
# @Email    : yangtianyu92@126.com
from filiter_infomation.template_filiter import template


re_temp = '<section class="mR1 fl">(.*?)</section>'

website = "中国贸易投资环境信息网"


if __name__ == '__main__':
    template(table="criterion2018", re_temp=re_temp, website=website)
