import sys
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
	url = 'http://www.piaotian.com/html/8/8767/5648381.html'
	req = requests.get(url=url)
	html = req.text
	bf = BeautifulSoup(html, 'html.parser')
	text = bf.find_all('html')
	print(text[0].text.replace('\xa0'*4, '\n\n'))