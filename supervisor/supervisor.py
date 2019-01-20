#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 23:03
# @Email    : yangtianyu92@126.com
import subprocess, time, sys

TIME = 10  # 程序状态检测间隔（单位：分钟）
CMD = "C:\\Users\\888\\PycharmProjects\\recall0Information\\save_html_to_mysql.py"  # 需要执行程序的绝对路径，支持jar 如：D:\\calc.exe 或者D:\\test.jar


# 监控运行状态， 如果失败15S后自动重启。
class AutoRun():
    def __init__(self, sleep_time, cmd):
        self.sleep_time = sleep_time
        self.cmd = cmd
        self.ext = (cmd[-3:]).lower()  # 判断文件的后缀名，全部换成小写
        self.p = None  # self.p为subprocess.Popen()的返回值，初始化为None
        self.index_file = r"C:\Users\888\PycharmProjects\recall0Information\urlLists\2018count.txt"
        self.run()  # 启动时先执行一次程序

        try:
            while 1 and self.judge_right():
                time.sleep(sleep_time)  # 休息10分钟，判断程序状态
                self.poll = self.p.poll()  # 判断程序进程是否存在，None：表示程序正在运行 其他值：表示程序已退出
                if self.poll is None:
                    print("运行正常")
                else:
                    print("未检测到程序运行状态，准备启动程序")
                    self.run()
        except KeyboardInterrupt as e:
            print("检测到CTRL+C，准备退出程序!")
            #            self.p.kill()                   #检测到CTRL+C时，kill掉CMD中启动的exe或者jar程序

    def judge_right(self):
        with open(str(self.index_file), "r") as f:
            index = f.read()
        if int(index) > 1263:
            return False
        else:
            return True

    def run(self):
        if self.ext == ".py":
            print('start OK!')
            self.p = subprocess.Popen(['python', '%s' % self.cmd],
                                      stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, shell=False)

        else:
            pass


if __name__ == '__main__':
    app = AutoRun(TIME, CMD)