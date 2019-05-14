import requests, json, sys, time
from contextlib import closing

class get_photos(object):
	"""docstring for get_photos"""
	def __init__(self):
		self.photo_id = []
		self.download_server = 'https://unsplash.com/photos/xxx/download?force=true'
		self.target = 'http://unsplash.com/napi/feeds/home'
		self.headers = {'authorization':'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'}
		
	def get_ids(self):
		reques = requests.get(url=self.target, headers=self.headers, verify=False)
		html = json.loads(reques.text)
		next_page = html['next_page']
		print('下一页地址：'+next_page)
		for each in html['photos']:
			print('图片ID：'+each['id'])
			self.photo_id.append(each['id'])
			time.sleep(1)

		# 获取后续4页的图片
		for i in range(4):
			reques = requests.get(url=next_page, headers=self.headers, verify=False)
			html = json.loads(reques.text)
			next_page = html['next_page']
			for each in html['photos']:
				print('图片ID：'+each['id'])
				self.photo_id.append(each['id'])
			time.sleep(1)

	def download(self, photo_id, filename):
				headers = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36'}
				target = self.download_server.replace('xxx',photo_id)
				with closing(requests.get(url=target, headers=headers, verify=False, stream=True)) as r:
					with open('%d.jpg' % filename, 'ab+') as f:
						for chunk in r.iter_content(chunk_size=1024):
							if chunk:
								f.write(chunk)
								f.flush()

if __name__ == '__main__':
	gp = get_photos()
	print('获取图片链接中。。。')
	gp.get_ids()
	print('下载图片中。。。')
	for i in range(len(gp.photo_id)):
		print('  正在下载地%d张图片  ' % (i+1))
		# gp.download(gp.photo_id[i], (i+1))
	print('下载结束！')