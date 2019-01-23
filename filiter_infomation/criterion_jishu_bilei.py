#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 17:11
# @Email    : yangtianyu92@126.com
from filiter_infomation.template_filiter import template


re_temp = '<div class="xxxq_text_left">(.*?)<div class="fenx_con">'

website = "技术壁垒资源网"


if __name__ == '__main__':
    template(table="criterion2018", re_temp=re_temp, website=website)