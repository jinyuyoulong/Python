import sys
import requests
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
	url = 'http://www.530p.com/lingyi/feizhengchangrenleiyiwenlu-179179/19800483.htm'
	req = requests.get(url=url)
	html = req.text
	bf = BeautifulSoup(html, 'html.parser')
	# page = bf.find_all('p', class_='Readpage')
	text = bf.find_all('div', id='cp_content')
	# bf=BeautifulSoup(text[0].html, 'html.parser')
	# text_p = bf.find_all('p')

	# m_writer(content)
	# print(content.encode('gbk'))
	# print(content.replace('\xa0'*2, '&&'))
	# print(content.encode().decode('gbk'))
	
	print(text[0].text.replace('。', '。\n\n'))

def m_writer(str):
	if (len(str) < 2):
		return
	file_path = 'content.html'
	with open(file_path, 'a', encode='gbk') as f:
		f.writelines(str)