import sys
from bs4 import BeautifulSoup
import requests
import lameixs_menu

def main():
	# urls = lameixs_menu.getURLs()
	url = 'http://m.lameixs.com/reader/77204/9491360.html'
	content = getContent(url)
	# setDoc(content)

	# text = content.replace('<br/><br/>','\n')
	# print(text)
	# nextUrl = bs.find_all('p',id='Readpage');
	# content = bs.find_all('div',id='node-content');
	# content1 = content[0]
	# print(type(content1))
	# print(content[0].text.replace('。','.\n'));
	# print(nextUrl);

def getNextURL(bs):
	return bs.findAll('a',id='pb_next')[0]['href']

def getContent(url):
	headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
	}
	response = requests.get(url=url)
	if(response.status_code == 404):
		print('这是个错误网址')
		return []
	print('正在打开 ',url)

	response.coding = 'utf-8'
	content = response.content
	bs = BeautifulSoup(content,'lxml');
	nextUrl = getNextURL(bs)
	content = bs.findAll('div',id='nr1')[0];
	# print(type(content.get_text()))
	text = content.get_text()
	text = text.replace('    ','\n')
	# print(text)
	return text,nextUrl


#传入字符串 写入文件；标题为l[0]
def setDoc(l,fileName):
    if(len(l) < 2):
        return
    file_s = fileName+'.txt'
    file = open(file_s, 'a', encoding='utf-8')
    file.write(l)
    # for i in l:
    #     file.write('\t')
    #     for ii in i.split('    '):
    #         file.write(ii)
    #     file.write('\n')

if __name__ == '__main__':
	main()