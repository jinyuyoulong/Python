#coding: utf-8
import re
import bs4
from bs4 import BeautifulSoup

#function: soup.select()
soup = BeautifulSoup(open("index.html"), "lxml")

# （1）通过标签名查找
# print soup.select('title')
# （2）通过类名查找
# print soup.select('.sister')
# （3）通过 id 名查找
# print soup.select('#link1')
# （4）组合查找 ：查找<p>中id=link1 的结果
# print soup.select('p #link1')
# 直接子标签查找
# print soup.select('head > title')
# （5）属性查找 
# 查找时还可以加入属性元素，属性需要用中括号括起来，
# 注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到
# print soup.select('a[class="sister"]')
# 属性+组合 不在同一节点的空格隔开，同一节点的不加空格
# print soup.select('p a[href="http://example.com/elsie"]')

print type(soup.select('title'))
print soup.select('title')[0].get_text()

for title in soup.select('title'):
	print title.get_text()