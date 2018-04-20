#coding:utf-8
import urllib2
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Referer": "http://www.zzsggzy.com/jsgc/004001/subpage.html"
}
url = "http://www.zzsggzy.com/jsgc/004001/subpage.html"
urlroot = "http://www.zzsggzy.com"

req = urllib2.Request(url, headers=headers)
res = urllib2.urlopen(req).read()
soup = BeautifulSoup(res, 'lxml')
li_list = soup.find_all('li', class_="ewb-com-item clearfix")
for li in li_list:
    link = urlroot + li.find('a')['href']
    title = li.find('a').text.replace(" ", "")
    time = li.find('span').text.replace(" ", "")
    print link
    print title
    print time



