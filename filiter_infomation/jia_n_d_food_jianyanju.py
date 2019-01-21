#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 23:22
# @Email    : yangtianyu92@126.com
from filiter_infomation.template_filiter import template


re_temp = '<main role="main" property="mainContentOfPage" \
class="col-md-9 col-md-push-3 -tv-ignore:E681,W620">(.*?)</main>'

website = "加拿大食品检验局网站"


if __name__ == '__main__':
    template(table="recall2018", re_temp=re_temp, website=website)