#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 10:47
# @Email    : yangtianyu92@126.com
import requests
import re

url = "http://tbt.sist.org.cn/cslm/omrassfzh/201811/t20181113_2213051.html"

header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
 'Cache-Control': 'max-age=0',
 'Connection': 'keep-alive',
 'Cookie': '_trs_uv=jp7qzq0w_1800_d2xg; _trs_ua_s_1=jr1f1l5i_1800_azoz; '
           'Hm_lvt_319ed1fe12668aac02ca463fb22bcb8d=1547777975; '
           'Hm_lpvt_319ed1fe12668aac02ca463fb22bcb8d=1547778844',
 'Host': 'tbt.sist.org.cn',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

response = requests.get(url)
response.encoding