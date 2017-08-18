# -*- coding:utf-8 -*-
import urllib, re

#第一步获取网页源代码
url = 'http://www.uctxt.com/book/17/17785/'
html = urllib.urlopen(url).read()
reg = re.compile(r'<dd><a href=(.*?)>(.*?)</a></dd>',re.S)
items = re.findall(reg, html)

dataArr = []
for i in items:
	contentURL = url+i[0]
	item = 'title: '+i[1]+'url: '+ contentURL
	dataArr.append(item)
	

with open('/Users/fans/Developer/Python/github/Python/spider/uctxt_menu.txt','w') as f:
		f.write(str(dataArr))
		f.close()
