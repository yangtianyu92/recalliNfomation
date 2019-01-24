#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 17:11
# @Email    : yangtianyu92@126.com
from filiter_infomation.template_filiter import template


re_temp = '<div class="content" id="article">(.*?)<div class="wzsj">'

website = "食品伙伴网"


if __name__ == '__main__':
    template(table="criterion2018", re_temp=re_temp, website=website)
