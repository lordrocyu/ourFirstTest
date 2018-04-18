#coding:utf-8

import urllib2
import json
import sys



url = "http://www.hfggzy.com:7090/fulltextsearch/rest/getfulltextdata?format=json&rmk3=029002001001&pn=0&rn=40&cl=150"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Refer": "http://www.hfggzy.com:7090/search/fullsearch.html?wd=&rmk1=&rmk2=&rmk3=029002001001"
}

req = urllib2.Request(url, headers=headers)
res = urllib2.urlopen(req).read()
res_d = json.loads(res)
result = res_d['result']['records']

for i in result:
    print "======"
    print i['title']
    print i['link']
    print i['date']
    print "------"


