# -*- coding:utf-8 -*-
import urllib, re

#第一步获取网页源代码
url = "http://www.uctxt.com/book/17/17785/"
html = urllib.urlopen(url).read()
reg = re.compile(r'<dd><a href=(.*?)>(.*?)</a></dd>',re.S)
items = re.findall(reg, html)

for i in items:
	print 'page:'+i[0]+'title: '+i[1]
