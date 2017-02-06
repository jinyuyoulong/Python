#coding: utf-8
import bs4
from bs4 import BeautifulSoup

# Tag
# NavigableString
# BeautifulSoup
# Comment

soup = BeautifulSoup(open('index.html'), "lxml")

# print soup.prettify()#格式化输出
# Tag 是什么？通俗点讲就是 HTML 中的一个个标签
# print soup.title
# print soup.head
# print soup.a
# print soup.p

#tag name
# print soup.name
# print soup.head.name

#tag attrs
#print soup.p.attrs #{'class': ['title'], 'name': 'dromouse'}
# print soup.p['class'] #单独获取属性值
# print soup.p.get('class') #单独获取属性值

#soup.p['class'] = "newClass" #修改属性值

# del soup.p['class'] #删除属性

# NavigableString
# print soup.p.string 

# BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag
# print type(soup.name)
# print soup.name
# print soup.attrs

# Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号
# print soup.a
# print soup.a.string
# print type(soup.a.string)
# if type(soup.a.string)!=bs4.element.Comment:
# 	print soup.a.string


#遍历文档树
# .contents 返回列表
#print soup.head.contents

# .children 返回一个 list 生成器对象 遍历获取所有子节点
# print soup.head.contents[0] 
# print soup.head.children
# for child in soup.body.children:
# 	print child

# .descendants 所有子孙节点
# for child in soup.descendants:
# 	print child

# 如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
# for string in soup.strings:
# 	print(repr(string))

# 使用 .stripped_strings 可以去除多余空白内容
# for string in soup.stripped_strings:
# 	print(repr(string))

# 父节点 .parent
# p = soup.p
# print p.parent.name
# content = soup.head.title.string
# print content.parent.name

# 全部父节点 .parents
# content = soup.head.title.string
# for parent in content.parents:
# 	print parent.name

# 同级节点 .next_sibling  .previous_sibling 属性
# print soup.p.next_sibling
# print soup.p.previous_sibling
# print soup.p.next_sibling.next_sibling

# 全部同级节点
# for sibling in soup.a.next_siblings:
# 	print(repr(sibling))

# 前后节点 .next_element .previous_sibling 在所有节点，不分层次
# print soup.head.next_element
# for element in soup.body.next_elements:
# 	print (repr(element))
	
