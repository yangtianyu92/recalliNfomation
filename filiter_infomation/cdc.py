from filiter_infomation.template_filiter import template


re_temp = '<div id="content">(.*?)<!-- /end #content -->'

website = "疾病控制保护中心"


if __name__ == '__main__':
    template(table="epidemic2018", re_temp=re_temp, website=website)

