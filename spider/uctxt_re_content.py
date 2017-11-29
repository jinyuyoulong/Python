# -*- coding:utf-8 -*-
import re, urllib

url = 'http://www.uctxt.com/book/17/17785/4608672.html'
html = urllib.urlopen(url).read()
reg = re.compile(r'<div id="content">(.*?)</div>',re.S)
content = re.findall(reg, html)

print content