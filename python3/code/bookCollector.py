 # -*- coding:UTF-8 -*-
import requests, sys
from bs4 import BeautifulSoup

    #     类说明:下载《笔趣看》网小说《一念永恒》
    # Parameters:
    #     无
    # Returns:
    #     无
    # Modify:
    #     2017-09-13
    
class downloader(object):
	"""docstring for downloader"""
	def __init__(self):
		super(downloader, self).__init__()
		self.server = 'http://www.biqukan.com'
		self.target = 'http://www.biqukan.com/1_1094'
		self.names = [] #存放章节名
		self.content = [] #存放内容
		self.urls = [] #存放链接
		self.num = 0 #记录总章节数

		
	def get_content(self, target):
		req = requests.get(url=target)
		html = req.text
		bf = BeautifulSoup(html, "html.parser")
		texts = bf.find_all('div', class_ = 'showtxt')
		texts = texts[0].text.replace('\xa0'*8,'\n\n')
		return texts

	def get_titles(self):
		req = requests.get(url=self.target)
		html = req.text
		div_bf = BeautifulSoup(html, 'html.parser')
		div = div_bf.find_all('div', class_ = 'listmain')
		a_bf = BeautifulSoup(str(div[0]), 'html.parser')
		a = a_bf.find_all('a')
		self.num = len(a[15:])
		# print(a)
		for each in a[15:]:
			self.names.append(each.string)
			self.urls.append(self.server+each.get('href'))

	def writer(self, name, path, text):
		write_flag = True
		with open(path, 'a', encoding='utf-8') as f:
			f.write(name + '\n')
			f.writelines(text)
			f.write('\n\n')

if __name__ == '__main__':
	dl = downloader()
	dl.get_titles()
	print('开始下载。。。')
	for i in range(dl.num):
			# print(dl.get_content(dl.urls[i]))
			dl.writer(dl.names[i], '一念永恒.txt',dl.get_content(dl.urls[i]))	
			sys.stdout.write("\r   已下载%.3f%%" % float(i/dl.num))
			sys.stdout.flush()
	print('下载完毕!')