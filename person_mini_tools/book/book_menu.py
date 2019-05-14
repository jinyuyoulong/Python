import requests
from bs4 import BeautifulSoup

url = 'http://www.530p.com/xuanhuan/qingyunian-15152/'
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
}
response = requests.get(url,headers=headers)
response.coding = 'utf-8'
html = response.text
response_content = response.content
#python3 默认使用Unicode，这里使用content二进制流进行解析,html 显示汉字乱码
bf = BeautifulSoup(response_content,'html.parser')
content = bf.find_all('div',class_='clc')

for item in content:
	a = item.a
	title = a.text
	the_id = a['href']
	str_print = title + ' \t' + the_id
	print(str_print)
