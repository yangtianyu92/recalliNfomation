#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 17:19
# @Email    : yangtianyu92@126.com
from multiprocessing import Pool
import requests
import time
from bs4 import BeautifulSoup
import re
import json
import random
requests.adapters.DEFAULT_RETRIES = 3

header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
 'Cache-Control': 'max-age=0',
 'Connection': 'keep-alive',
 'Cookie': 'td_cookie=1586371308; '
           '__gads=ID=6efab4d2cfdbf3dd:T=1545724958:S=ALNI_MYm731z5NsV_HMjjpwJOsP1eYQLJw; '
           'Hm_lvt_2aeaa32e7cee3cfa6e2848083235da9f=1545724899,1545724907,1547798446,1548218310; '
           '__51cke__=; '
           'yunsuo_session_verify=0a2f72261c6d64e8c7c14d6429c1f182; '
           'Hm_lpvt_2aeaa32e7cee3cfa6e2848083235da9f=1548223783; '
           '__tins__1636283=%7B%22sid%22%3A%201548223783146%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201548225583146%7D; '
           '__51laig__=13',
 'Host': 'news.foodmate.net',
 'If-Modified-Since': 'Fri, 18 Jan 2019 07:22:44 GMT',
 'If-None-Match': 'W/"5c417ec4-9c3d"',
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


# 获取IP池内Ip
def get_proxy():
    with open(r"C:\Users\888\PycharmProjects\recall0Information\IP_proxy_connection\ip_pool.json", "r") as f:
        return json.loads(f.read())


def get_html(url, encode="utf-8"):
    proxy_ips = get_proxy()
    r_index = random.randint(0, 4)
    ip_use = proxy_ips[r_index]
    proxy_dict = {"http": str(ip_use["ip"]) + ":" + str(ip_use["port"])}
    try:
        response = requests.get(url, headers=header, proxies=proxy_dict, timeout=5)
    except:
        
        raise TimeoutError

    response.encoding = encode
    print(clear_html(response.text)[200:])
    return response.text, url


def muliti_down(urls):
    muliti_pool = Pool(processes=4)
    result_html_list = muliti_pool.map(get_html, urls)
    return result_html_list


"""
让我们测试下多进程的优势，下载速度提升了60%
"""


if __name__ == '__main__':
    print(get_proxy()[1])
    """
    time_begin = time.time()
    for url in urls:
        print(get_html(url))
    time_end = time.time()
    print("time is ~~~~~---" + str(time_end - time_begin))"""