#coding: utf-8
from pyquery import PyQuery as pq

# http://blog.csdn.net/cnmilan/article/details/8727308

# url = 'http://www.uctxt.com/index/type-1-1'

doc = pq(filename='uctxt.html')
# with open('/Users/fans/Developer/Python/pythonStudy/spider/uctxt.html','w') as f:
# 	f.write(str(doc))
# 	f.close()

section = doc.find('section')
ul = section('ul')
li = section('li')
print section('ul').children().length
count = ul.children().length

for i in xrange(1,count):
	title = li.eq(i)('.class')
	name = li.eq(i)('.name')
	other = li.eq(i)('.other')
	print title.text()
	print name.text()
	print other.text()
	print '\n'
	

