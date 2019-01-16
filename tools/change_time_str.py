#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 11:45
# @Email    : yangtianyu92@126.com
import datetime
import time


# 更改时间格式类型
class ChangeTime:
    """
    :param the raw of date_untreated, raw format
    tutorial inspect：
        date_raw = "11/23/2018"
        ct = ChangeTime(date_raw, "%m/%d/%Y")
        result_dict["Date"] = ct.mysql_time(3)
    """
    def __init__(self, t, time_format):
        self.time = time.strptime(t, time_format)

    def mysql_time(self, info_numbers):
        """
        :param info_numbers: how many date_info in the untreated raw_date
        :return: mysql_used datetime
        """
        mysql_date = datetime.datetime(*self.time[:info_numbers])
        return mysql_date.strftime("%Y-%m-%d %H:%M:%S")

