#coding:utf-8

import urllib2
from bs4 import BeautifulSoup
url = "http://www.szdesigncenter.org/?cat=203"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Referer": "http://www.szdesigncenter.org/"
}


req = urllib2.Request(url, headers=headers)
res = urllib2.urlopen(req).read()
soup = BeautifulSoup(res, 'lxml')
div_articles = soup.find_all("div", class_="article")
result = []
for div_article in div_articles:
    dic = {}
    dic['link'] = div_article.find('a')['href']
    dic['title'] = div_article.find('a').text
    result.append(dic)
    print dic['title']
    print dic['link']
    print '===================='
