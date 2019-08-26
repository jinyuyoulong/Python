import requests
import re
from bs4 import BeautifulSoup

# 解析本地文本

# 读取文件
response_content = open("/Users/fanjinlong/dev/myProducts/blog/v5u.win/it-keyword.html")
#python3 默认使用Unicode，这里使用content二进制流进行解析,html 显示汉字乱码
bf = BeautifulSoup(response_content,'html.parser')
content = bf.find_all('div',class_='row')
f = open('out.html', 'w')
for item in content:
	# print(item)
	print("=======")
	category = item.span
	categoryValue = category.text
	categoryDes = category['title']
	
	f.write('<span class="category">'+categoryValue+'</span><br/>')
	f.write('\n')

	print('category：'+categoryValue + ' ')
	# print(categoryDes)
	# pattern = re.compile(r'<p class="tooltops-text">*</p>')
	# match = re.search(pattern,categoryDes)
	# if match:
	# 	print(match.group())
	ul = item.find_all('a',class_='hoverTooltip')
	for lis in ul:
		print(lis.text+' ')
		print(lis['href'])
		f.write('<a class="item" href="'+lis['href']+'">'+lis.text+'</a>&nbsp;')
		f.write('\n')
	
	# title = a.text
	# the_id = a['href']
	# print(str_print)

	f.write('<hr>')
	f.write('\n')
	print("--------")
f.close()