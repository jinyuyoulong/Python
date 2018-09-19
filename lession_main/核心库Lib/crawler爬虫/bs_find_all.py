#coding: utf-8
import bs4
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open("index.html"), "lxml")

# print soup.find_all('b')
# for tag in soup.find_all(re.compile("^b")):
#  	 print(tag.name)
# print soup.find_all(["a","b"])
# for tag in soup.find_all(True):
# 	print(tag.name)

# def has_class_but_no_id(tag):
# 	return tag.has_attr('class') and not tag.has_attr('id')
# print soup.find_all(has_class_but_no_id)

# keyword 参数
# 注意：如果一个指定名字的参数不是搜索内置的参数名,
# 搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性
# print soup.find_all(id='link2')

# 如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性
# print soup.find_all(href=re.compile("elsie"))

# 使用多个指定名字的参数可以同时过滤tag的多个属性
# for item in soup.find_all(href=re.compile("elsie"), id='link1'):
# 	print item

# 用 class 过滤，不过 class 是 python 的关键词，需要使用class_
# for item in soup.find_all("a",class_="sister"):
#  	print item 

# 有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性
# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>',"lxml")
# print data_soup.find_all(data-foo = "value")
# 但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
# print data_soup.find_all(attrs={"data-foo":"value"})

# text 参数
# 通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True
# print soup.find_all(text="Elsie")
# print soup.find_all(text=["Tillie","Lacie","Elsie"])
# print soup.find_all(text=re.compile("Dormouse"))

# limit 参数
# print soup.find_all("a",limit=2)

# recursive 参数（递归）
# 如果只想搜索tag的 -->直接子节点,可以使用参数 recursive=False
# print soup.html.find_all("title")
# print soup.html.find_all("title", recursive=False)

