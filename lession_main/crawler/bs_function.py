#coding: utf-8
import bs4
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(open("index.html"),"lxml")

# find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
# find_all( name , attrs , recursive , text , **kwargs )
# print soup.find_all('a')

# 传正则表达式
# for tag in soup.find_all(re.compile("^b")):
# 	print(tag.name)

# 传列表
# print soup.find_all(["a","b"])

# True参数 True 可以匹配任何值,
# 查找到所有的tag,但是不会返回字符串节点
# for tag in soup.find_all(True):
# 	print(tag.name)

# 传方法
# 如果包含 class 属性却不包含 id 属性,那么将返回 True
def has_class_but_no_id(tag):
	return tag.has_attr('class') and not tag.has_attr('id')
print soup.find_all(has_class_but_no_id)