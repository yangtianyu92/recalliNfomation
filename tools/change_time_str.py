#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 11:45
# @Email    : yangtianyu92@126.com
import datetime
import time


# 更改时间格式类型
class ChangeTime:
    def __init__(self, t, time_format):
        self.time = time.strptime(t, time_format)

    def mysql_time(self, info_numbers):
        mysql_date = datetime.datetime(*self.time[:info_numbers])
        return mysql_date.strftime("%Y-%m-%d %H:%M:%S")