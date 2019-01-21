#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 22:54
# @Email    : yangtianyu92@126.com
from filiter_infomation.template_filiter import template

re_temp = '<div class="grid-12 span-12 breake_word widthfull" id="awr_details_container">(.*)<div class="clear"></div>'
website = "加拿大健康网"


if __name__ == '__main__':
    template(table="recall2018", re_temp=re_temp, website=website)
