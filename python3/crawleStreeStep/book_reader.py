import sys
import requests
from bs4 import BeautifulSoup
import re
# import urllib.requests


def main():	
	url = getURL()
	headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
	}
	req = requests.get(url=url,headers=headers)
	req.coding = 'utf-8'
	bf = BeautifulSoup(req.content, 'lxml')#python3 默认使用Unicode，这里使用content二进制流进行解析
	# page = bf.find_all('p', class_='Readpage')
	text = bf.find_all('div', id='cp_content')
	next_page = bf.find('a',id='nextLink')
	# bf=BeautifulSoup(text[0].html, 'html.parser')
	# text_p = bf.find_all('p')

	# print(content.replace('\xa0'*2, '&&'))
	# print(content.encode().decode('gbk'))
	
	print(text[0].text.replace('。' , '。\n\n'))#text没有换行，去掉了一切标签元素，只等使用。作为分割符

	href = next_page.get('href')
	print('url = \'http://www.530p.com%s\'' % href)
	
	m_writer(next_page)

def m_writer(next_page_str):
	if (len(next_page_str) < 2):
		return
	print(next_page_str)
	# return

	# file_path = 'content.html'
	# with open(file_path, 'a', encode='gbk') as f:
	# 	f.writelines(str)

def getURL():
	return 'http://www.530p.com/xuanhuan/moshiweicheng-182471/26251954.htm'
	
if __name__ == '__main__':
	main()