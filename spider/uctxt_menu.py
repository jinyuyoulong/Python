#coding: utf-8
from pyquery import PyQuery as pyq
import uctxt_content

url = "http://www.uctxt.com/book/17/17785/"
doc = pyq(url)
# print doc
dl = doc('dl')
titles = dl('a')
count = dl.children().length
urlContents = []
for x in xrange(0,count):
	a = titles.eq(x)
	href = a.attr('href')
	urlContent = url+href
	urlContents.append(urlContent)

for k,v in enumerate(urlContents):
	print k,v
contentURL_1 = urlContents[0]
print contentURL_1

# contentObj = PaserUCTxtContent(urlContents[0])
# contentObj.paser()
	
