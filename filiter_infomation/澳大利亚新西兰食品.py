#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 22:54
# @Email    : yangtianyu92@126.com
from filiter_infomation.template_filiter import template

re_temp = '<div id="PrintPreviewArea">(.*)PageContentManager">'
website = "澳大利亚新西兰食品标准局"


if __name__ == '__main__':
    template(table="recall2018", re_temp=re_temp, website=website)

