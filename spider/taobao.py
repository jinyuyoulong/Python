#coding: utf-8
from pyquery import PyQuery as pq

# doc = pq(url=r'https://www.taobao.com/markets/tbhome/market-list')
doc = pq(filename='dome.html')
# with open('/Users/fans/Developer/Python/pythonStudy/spider/dome.html','w') as f:
# 	f.write(str(doc))
# 	f.close()

div = doc.find('ul')
print div
