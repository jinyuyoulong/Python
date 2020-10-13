import sys
from bs4 import BeautifulSoup
import requests

def main():
	getURLs()


def getURLManus():
	urlmanus = []
	for x in range(1,11):
		url = 'http://m.lameixs.com/reader/77204/list'+str(x)+'.html'
		urlmanus.append(url)
	return urlmanus

def getURLs():
	manus = getURLManus()
	urls = []
	for item in manus:
		# print('manu:'+item)
		hrefs = getHref(item)
		urls.extend(hrefs)
	# print(urls)
	return urls

def getHref(url):
	headers = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
		}
	response = requests.get(url=url)
	response.coding = 'utf-8'
	bs = BeautifulSoup(response.content,'lxml')	
	chapter = bs.find_all('a');
	hrefs = []
	for x in range(9,(len(chapter)-5)):
		item = 'http://m.lameixs.com'+chapter[x]['href']
		hrefs.append(item)
	return hrefs

if __name__ == '__main__':
	main()