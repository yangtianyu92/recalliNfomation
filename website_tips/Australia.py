#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 15:31
# @Email    : yangtianyu92@126.com
import requests
import re
from linkmysql import link_mysql_write
import datetime
from tools.change_time_str import ChangeTime


header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
 'Cache-Control': 'max-age=0',
 'Connection': 'keep-alive',
 'Cookie': '__utmz=219145102.1547792022.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); '
           '__utma=219145102.177749145.1547792022.1547792022.1547969415.2; '
           '__utmc=219145102; __utmt=1; WSS_FullScreenMode=false; '
           '__utmb=219145102.3.10.1547969415',
 'Host': 'www.foodstandards.gov.au',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

url_australia = "http://www.foodstandards.gov.au/industry/foodrecalls/recalls/Pages/default.aspx"


for i in range(1, 22):
    url_australia_page = url_australia + "?page=" + str(i)
    response = requests.get(url=url_australia_page, headers=header)

    create_time = re.findall('right">(.*?)</div><h3>', response.text)
    ct = [ChangeTime(time, "%d/%m/%Y").mysql_time(3) for time in create_time]

    hrefs = re.findall('</div><h3><a href=\"(.*?)\"', response.text)

    titles = re.findall('</div><h3><a href=\".*?\">(.*?)</a></h3></td></tr><tr valign', response.text)

    website_name = "澳大利亚新西兰食品标准局"

    datetime_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(i)
    for j in range(9):
        sql_raw = """insert into recall2018 (ThirdReport_Title, ThirdReport_Url, ThirdReport_CreateTime,\
        ThirdReport_GetherTime, ThirdReport_SiteName, ThirdReport_InfoType) values
        ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}");
        """
        if "2019" in ct[j]:
            a1 = sql_raw.format(titles[j], hrefs[j],  ct[j], datetime_now, website_name, "召回")
            link_mysql_write(a1)