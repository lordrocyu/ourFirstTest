#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.chinabidding.cn/search/searchzbw/search2?areaid=&keywords=%E8%AE%BE%E8%AE%A1&page=1&categoryid=&rp=44&table_type=3&b_date="
urlroot = "https://www.chinabidding.cn"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Referer": "https://www.chinabidding.cn/search/searchzbw/search2?keywords=%E8%AE%BE%E8%AE%A1&table_type=3&areaid=&categoryid=&b_date="
}
def getattr(url,headers):
    req = urllib2.Request(url, headers=headers)
    res = urllib2.urlopen(req).read()
    soup = BeautifulSoup(res, 'lxml')
    tr_body = soup.find_all("tr", class_=re.compile("listrow?"))
    for tr in tr_body:
        td = tr.find_all('td')
        time = td[6].find("div").text
        time = time[:10]
        a_body = tr.find('a')
        title = a_body.text
        link = urlroot + a_body["href"]
        print title
        print link
        print time


for i in range(1, 4):
    print "This is page %s" % i
    url = "https://www.chinabidding.cn/search/searchzbw/search2?areaid=&keywords=%E8%AE%BE%E8%AE%A1&page=" + str(i) + "&categoryid=&rp=44&table_type=3&b_date="
    getattr(url, headers)
    print "This is page %s end" % i