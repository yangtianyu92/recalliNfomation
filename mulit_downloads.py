#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 17:19
# @Email    : yangtianyu92@126.com
from multiprocessing import Pool
import requests
import time
from bs4 import BeautifulSoup
import re

header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
 'Cache-Control': 'max-age=0',
 'Connection': 'keep-alive',
 'Cookie': '_trs_uv=jp7qzq0w_1800_d2xg; '
           'Hm_lvt_319ed1fe12668aac02ca463fb22bcb8d=1547777975,1547803024,1548002565; '
           'Hm_lpvt_319ed1fe12668aac02ca463fb22bcb8d=1548002565',
 'Host': 'www.fsis.usda.gov',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

header2 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
 'Cache-Control': 'max-age=0',
 'Connection': 'keep-alive',
 'Cookie': '__utmz=219145102.1547792022.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); '
           '__utmc=219145102; WSS_FullScreenMode=false; '
           '__utma=219145102.177749145.1547792022.1547972235.1547987103.4; '
           '__utmt=1; __utmb=219145102.1.10.1547987103',
 'Host': 'www.foodstandards.gov.au',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

urls = ["http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com"]


# 清理html网页文件
def clear_html(html):
    soup = BeautifulSoup(html, 'lxml')
    clear_soup = re.sub('[\.\!\/_$%^*(\"\')—?【】“”！，。？、~@#￥…&（）\n\t\r;]', '', soup.text)
    return clear_soup


def get_html(url, encode="utf-8"):
    response = requests.get(url, headers=header)
    response.encoding = encode
    return response.text, url


def muliti_down(urls):
    muliti_pool = Pool(processes=4)
    result_html_list = muliti_pool.map(get_html, urls)
    return result_html_list


"""
让我们测试下多进程的优势，下载速度提升了60%
"""


if __name__ == '__main__':

    time_begin = time.time()
    for url in urls:
        print(get_html(url))
    time_end = time.time()
    print("time is ~~~~~---" + str(time_end - time_begin))