#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 21:17
# @Email    : yangtianyu92@126.com
import re


def clear_atr(html):
    re_script = re.sub('<script.*?script>', '', html)
    re1 = re.sub('<.*?>', '', re_script)
    re2 = re.sub('[\.\!\/_$%^*(\"\')—?【】“”！，。？、~@#￥…&（）\n\r;]', '', re1)
    re3 = re.sub('nbsp', '', re2)
    re4 = re.sub('<style.*?style>', '', re3)
    return re4
