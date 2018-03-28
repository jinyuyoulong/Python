import requests
from bs4 import BeautifulSoup

url = 'http://www.530p.com/lingyi/feizhengchangrenleiyiwenlu-179179/'
response = requests.get(url)
html = response.text
bf = BeautifulSoup(html,'html.parser')
content = bf.find_all('div',class_='clc')

for item in content:
	title = item.text
	the_id = item['href']
	print(item)
	# print(the_id)