#coding:utf-8
from selenium import webdriver
import time
import sys
import re,json
reload(sys)
sys.setdefaultencoding('utf-8')
urlroot = "http://www.jszb.com.cn/JSZB/YW_info"
def print_line():
    lines = dr.find_elements_by_class_name("moreinfoline")
    info = {}
    for line in lines:
        for i in line.find_elements_by_css_selector('a'):
            time = line.find_elements_by_css_selector('td')[3].text
            p = re.compile(r'\"\.\.(.+?)\"')
            title = i.text
            link = i.get_attribute('onclick')
            link = urlroot + p.findall(link)[0]
            info["title"] = title
            info["link"] = link
            info["time"] = time
            print info
            print "-----------------"
            with open("spiderInfo.txt", 'ab+') as f:
                f.write(json.dumps(info))

dr = webdriver.Firefox()
dr.get("http://www.jszb.com.cn/JSZB/YW_info/ZhaoBiaoGG/MoreInfo_ZBGG.aspx?Type=%u8bbe%u8ba1")
print_line()
for i in range(2, 4):
    href = r"a[href*='javascript:__doPostBack']"
    print href
    pageIcons = dr.find_elements_by_css_selector(href)
    pageIcons[-2].click()
    time.sleep(5)
    print_line()
dr.close()