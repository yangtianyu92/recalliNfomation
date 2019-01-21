#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/18 9:12
# @Email    : yangtianyu92@126.com
from linkmysql import link_mysql_read, link_mysql_write
from save_html_to_mysql import base64_decode
import re
from filiter_infomation.clearAttr import clear_atr


# 过滤模板
def template(table, re_temp, website):
    sql_read_from_html = """
    select ThirdReport_Raw,ThirdReport_Url from {0} where ThirdReport_SiteName = "{1}"; 
    """.format(table, website)

    change_sql = """
    update """ + table + """ set ThirdReport_Content="{0}" where ThirdReport_Url="{1}";
    """

    list_content = link_mysql_read(sql_read_from_html)

    for index, dic in enumerate(list_content):
        html_test = base64_decode(list_content[index]['ThirdReport_Raw'])
        url = list_content[index]["ThirdReport_Url"]
        try:
            article = clear_atr(re.findall(re_temp, html_test, re.S)[0])
            print(article)
            sql_c = change_sql.format(article, url)
            link_mysql_write(sql=sql_c)
        except:
            print("正则出现问题")


if __name__ == '__main__':
    table = 'recall2018'
    re_temp = ' style="min-height:405px">(.*?)<div class="fenx_con">'
    website = "中国技术性贸易措施网"
    template(table=table, re_temp=re_temp, website=website)