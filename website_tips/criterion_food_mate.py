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
 'Cookie': '__gads=ID=6efab4d2cfdbf3dd:T=1545724958:S=ALNI_MYm731z5NsV_HMjjpwJOsP1eYQLJw; \
 Hm_lvt_2aeaa32e7cee3cfa6e2848083235da9f=1545724899,1545724907,1547798446,1548218310; \
 __51cke__=; yunsuo_session_verify=f26b4bb6885d0a600716ca313c595211; \
 Hm_lpvt_2aeaa32e7cee3cfa6e2848083235da9f=1548218853; \
 __tins__1636283=%7B%22sid%22%3A%201548218310024%2C%20%22vd%22%3A%\
 2011%2C%20%22expires%22%3A%201548220653344%7D; __51laig__=11',
 'Host': 'news.foodmate.net',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

url_foodMate = "http://news.foodmate.net/yujing/list_{}.html"

website_name = "食品伙伴网"


for i in range(1, 43):
    url_foodMate_page = url_foodMate.format(str(i))
    response = requests.get(url=url_foodMate_page, headers=header)
    response.encoding = "utf-8"
    create_time = re.findall('class="f_r px11 f_gray">(.*?)</span>', response.text)
    print(create_time)
    ct = [ChangeTime(time, "%Y-%m-%d %H:%M").mysql_time(3) for time in create_time]

    hrefs = re.findall('class="f_r px11 f_gray">.*</span><a href=\"(.*?)\"', response.text)

    titles = re.findall('target="_blank" title="(.*?)"', response.text)

    datetime_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(i)
    for j in range(49):
        sql_raw = """insert into criterion2018 (ThirdReport_Title, ThirdReport_Url, ThirdReport_CreateTime,\
        ThirdReport_GetherTime, ThirdReport_SiteName, ThirdReport_InfoType) values
        ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}");
        """
        if "2018" in ct[j]:
            a1 = sql_raw.format(titles[j], hrefs[j],  ct[j], datetime_now, website_name, "标准变更")
            link_mysql_write(a1)
