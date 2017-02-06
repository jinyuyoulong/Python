#coding: utf-8
from pyquery import PyQuery as pq
# 四种初始化方式
# 1 直接字符串
# doc = pq("<html></html>")
# 2 lxml.etree
# from lxml import etree
# doc = pq(etree.fromstring("<html></html>"))
# 3 直接传URL
# doc = pq('http://www.baidu.com')
# 4 传文件
doc = pq(filename='hello.html')
# print doc.html()
# print type(doc)
# li = doc('li')
# print type(li)
# print li.text()
print doc('li').children().length
## 属性 操作
# p = pq('<p id="hello" class="hello"></p>')('p')
# print p.attr("id")
# print p.attr("id","plop")
# print p.attr("id", "hello")
# print p.addClass('beauty')
# print p.removeClass('hello')
# print p.css('font-size', '16px')
# print p.css({'background-color': 'yellow'})

## DOM操作
# p = pq('<p id="hello" class="hello"></p>')('p')
# # 追加内容
# print p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>')
# print p.prepend('Oh yes!') 	#在p内容的首部添加内容
# d = pq('<div class="wrap"><div id="test"><a href="http://cuiqicai.com">Germy</a></div></div>')
# p.prependTo(d('#test'))	#在d中id=test标签后面添加p
# print p
# print d
# d.empty() #清空d中内容（只留下根标签）
# print d

## 遍历 items / lambda
# lis = doc('li')
# for li in lis.items():
# 	print li.html()
# print lis.each(lambda e: e)

## 网页请求
# print pq('http://cuiqingcai.com/', header={'user-agent': 'pyquery'})
# print pq('http://httpbin.org/post',{'foo': 'bar'}, method='post', verify=True)