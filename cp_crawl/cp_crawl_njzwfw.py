#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

urls = []
for i in range(4):
    url = "http://ggzy.njzwfw.gov.cn/njweb/fjsz/068001/068001001/" + str(i+1) + ".html"
    urls.append(url)


urlroot = "http://ggzy.njzwfw.gov.cn"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Referer": "http://ggzy.njzwfw.gov.cn/njweb/fjsz/buildService1.html"
}
for u in urls:
    req = urllib2.Request(u, headers=headers)
    res = urllib2.urlopen(req).read()
    soup = BeautifulSoup(res, 'lxml')

    div_articles = soup.find_all("li", class_="ewb-info-item2")

    for i in div_articles:
        result = i.find_all('div')
        type = result[2].find('p')['title']
        if type == u"设计":
            title = result[1].find('p')['title']
            price = result[3].find('p').text
            time = result[4].find('p').text
            link = i['onclick']
            p = re.compile(r'\'(.+?)\'')
            link_s = urlroot + p.findall(link)[0]
            print title
            print type
            print price
            print time
            print link_s

            print "================="
