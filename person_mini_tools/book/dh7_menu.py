import sys
from bs4 import BeautifulSoup
import requests

def main():
	# sex web site
	# www.d2hd2h.com
	url = 'http://www.dh7dh7.com/arttypehtml/2.html'
	headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
	}
	response = requests.get(url=url)
	response.coding = 'utf-8'
	bs = BeautifulSoup(response.content,'html.parser')	
	content = bs.find_all();
	# content = bs.find_all('div',id='node-content');
	# content1 = content[0]
	# print(type(content1))
	
	# aList = bs.find_all('a')
	# for x in aList:
	# 	print(x)
	
	print(content)

if __name__ == '__main__':
	main()