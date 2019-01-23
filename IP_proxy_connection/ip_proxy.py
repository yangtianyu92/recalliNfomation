#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 14:27
# @Email    : yangtianyu92@126.com
import requests
import time


class GetProxy:
    def __init__(self):
        self.url = "http://webapi.http.zhimacangku.com/getip?num=5&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
        self.response_ip = requests.get(self.url).json()

    @staticmethod
    def certify_ip(ips):
        for ip in ips:


    def phrase_ip(self, response):
        return response["data"]

    def ip_pool(self):
        while True:
            response_ip = requests.get(self.url).json()
            print(response_ip)
            with open("ip_pool.json", "a") as f:
                f.write(str(self.phrase_ip(response_ip)).replace("\'", "\""))
            time.sleep(300)


if __name__ == '__main__':
    gp = GetProxy()
    gp.ip_pool()
