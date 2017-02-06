#-*- coding: utf-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

page = 1
url = 'http://www.qiushibaike.com/text/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent' : user_agent}
try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	# print len(response.read())
	# print response.read()

	content = response.read().decode('utf-8')
	pattern = re.compile(r'<span>\D</span>',re.S)
	items = re.findall(pattern,content)
	#print items
	for item in items:
		print item
	 

except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason
