from filiter_infomation.template_filiter import template


re_temp = '<div class="zwdabox">(.*?)</table>'

website = "中国技术性贸易措施网"


if __name__ == '__main__':
    template(table="recall2018", re_temp=re_temp, website=website)