#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 11:24
# @Email    : yangtianyu92@126.com
import requests
import re
import datetime
from tools.change_time_str import ChangeTime
from linkmysql import link_mysql_write

url_fda = "https://www.fda.gov/Safety/Recalls/default.htm"

response = requests.get(url=url_fda)


def extra_fda(response):
    result_list = []
    result_dict = {
        "Date": "",
        "Brand": "",
        "Report_Href": "",
        "Product_Description": "",
        "Reason_Problem": "",
        "Company": "",
    }
    a = re.findall('data\": \[(.*)]', response.text, re.DOTALL)
    table = re.findall('\[(.*?)\]', a[0])[:-10]
    for array in table:
        table_list = array.split(",")
        date_raw = table_list[0].replace('\'', '')
        ct = ChangeTime(date_raw, "%m/%d/%Y")
        result_dict["Date"] = ct.mysql_time(3)
        brand = re.findall('>(.*)<', table_list[1])
        if brand != []:
            result_dict["Brand"] = brand[0]
        else:
            result_dict["Brand"] = "null"
        result_dict["Report_Href"] = "https://www.fda.gov" + re.findall('href=\"(.*?)\">', table_list[1])[0]
        result_dict["Product_Description"] = table_list[2].replace('\'', '')
        try:
            result_dict["Reason_Problem"] = table_list[3].replace('\'', '')
            result_dict["Company"] = table_list[4].replace('\'', '')
        except:
            result_dict["Reason_Problem"] = "null"
            result_dict["Company"] = "null"
        result_list.append(result_dict)
        result_dict = {}
    return result_list

print(extra_fda(response))