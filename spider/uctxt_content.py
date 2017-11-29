#coding: utf-8
import sys
from pyquery import PyQuery as pyq
# 
url = 'http://www.uctxt.com/book/17/17785/4608673.html'
# 解决写入本地 ASCII 编码不识别问题


class PaserUCTxtContent(object):
	"""docstring for PaserUCTxtContent"""
	def __init__(self, url):
		super(PaserUCTxtContent, self).__init__()
		self.url = url

	def paser():
		reload(sys)
		sys.setdefaultencoding('utf-8')

		doc = pyq(url,encoding="gbk")

		div = doc('div').filter('#main')
		title = div('h1')
		section = div('section')
		article = section('article')
		content = article('#content')
		string = content.html() 
		string = string.replace('<br/>',"\n")
		string = string.replace('&nbsp;',' ')
		string = string.replace('&#13;','\n')
		with open("/Users/fans/Developer/Python/pythonStudy/spider/content.txt",'w') as file:
			file.write(string)
			file.close()
		print string

paser = PaserUCTxtContent(url)