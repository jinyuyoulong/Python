import sys
from bs4 import BeautifulSoup
import requests

def main():
	# sex web site
	url = 'http://m.zhanzhekan1.cc/13_13718/all.html'
	headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
	}
	response = requests.get(url=url)
	response.coding = 'utf-8'
	bs = BeautifulSoup(response.content,'lxml')	
	content = bs.find_all();
	# content = bs.find_all('div',id='node-content');
	# content1 = content[0]
	# print(type(content1))
	print(content)

if __name__ == '__main__':
	main()