#coding: utf-8
from pyquery import PyQuery as pq
import urllib
import urllib2
import re
import bs4
from bs4 import BeautifulSoup
url = 'https://cnodejs.org/'

doc = pq(url,hander={'user-agent': 'pyquery'})
ass = doc('a')
for item in ass:
	print item

# response = urllib.urlopen(url)
# soup = BeautifulSoup(response, 'lxml')
# for item in soup.find_all(class_='topic_title'):
# 	print item.value

		