#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 21:17
# @Email    : yangtianyu92@126.com
import re


def clear_atr(html):
    re1 = re.sub('<.*?>', '', html)
    re2 = re.sub('[\.\!\/_$%^*(\"\')—?【】“”！，。？、~@#￥…&（）\n\r;]', '', re1)
    return re2
