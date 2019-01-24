#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 13:31
# @Email    : yangtianyu92@126.com
import requests
import re
from linkmysql import link_mysql_write
import datetime
from tools.change_time_str import ChangeTime
from tools.clearAttr2 import clear_atr
from save_html_to_mysql import base64_encode
from bs4 import BeautifulSoup

urls =  ['/salmonella/concord-11-18/index.html',
         '/salmonella/agbeni-11-18/index.html',
         '/salmonella/infantis-10-18/index.html',
         '/salmonella/newport-10-18/index.html',
         '/salmonella/enteritidis-09-18/index.html',
         '/salmonella/chicken-08-18/index.html',
         '/salmonella/reading-07-18/index.html',
         '/salmonella/sandiego-07-18/index.html',
         '/salmonella/mbandaka-06-18/index.html',
         '/salmonella/adelaide-06-18/index.html',
         '/salmonella/braenderup-04-18/index.html',
         '/salmonella/typhimurium-03-18/index.html',
         '/salmonella/typhimurium-02-18/index.html',
         '/salmonella/kratom-02-18/index.html',
         '/salmonella/montevideo-01-18/index.html',
         '/salmonella/coconut-01-18/index.html']

urls = ["https://www.cdc.gov" + ul for ul in urls]



header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
 'Cache-Control': 'max-age=0',
 'Connection': 'keep-alive',
 'Cookie': '',
 'Host': 'www.cdc.gov',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


website_name = "疾病控制保护中心"


for i in range(4, len(urls)):
    response = requests.get(url=urls[i], headers=header)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    create_time = re.findall('<span itemprop="dateModified">(.*?)</span>', response.text)
    print(create_time)
    ct = ChangeTime(create_time[0], "%B %d, %Y").mysql_time(3)
    print(ct)
    href = urls[i]

    title = soup.title.text
    print(title)
    datetime_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(i)
    sql_raw = """update epidemic2018 set ThirdReport_Title="{0}", ThirdReport_Url="{1}", ThirdReport_CreateTime="{2}",\
    ThirdReport_GetherTime="{3}", ThirdReport_SiteName="{4}", ThirdReport_InfoType="{5}", ThirdReport_Raw="{6}" \
    where ThirdReport_Url="{7}";
    """
    if "2018" in ct:
        a1 = sql_raw.format(title[:200], href,  ct, datetime_now, website_name, "标准变更", base64_encode(response.text), urls[i])
        print(a1)
        link_mysql_write(a1)



