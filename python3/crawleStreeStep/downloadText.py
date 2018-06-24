# -*- coding: utf-8 -*-
import re
import urllib.request as request  
from bs4 import BeautifulSoup  
import requests

# url = 'http://www.biquge.com/0_68/1066142.html'  
url = 'http://www.530p.com/xuanhuan/jiangye-146942/'  

def setSrr(url):
    if(requests.get(url).status_code == 404):
        print('这是个错误网址')
        return []
    print ('正在打开 ',url)    

    l  = []
    '''请求响应和不响应的处理'''
    response = request.urlopen(url)
    
    html = response.read()  
    soup = BeautifulSoup(html)
    item = soup.findAll('h1') 
    # get title
    title = re.match(r'(.*)<h1> (.*)</h1>(.*)', str(item) ,re.M|re.I).group(2)
    l.append(title.split(' ')[0])
    l.append(title)
    strings = soup.findAll('div', id="content")[0];
    for string in strings:
        st = string.__str__()
        if (len(st.split('<br/>')) > 1):
            pass
        else:
            l.append(st)
    return l
#strings.split()

#传入字符串 写入文件；标题为l[0]
def setDoc(l):
    if(len(l) < 2):
        return
    file_s = 'F:\\By\\August\\160828\\超品相师\\' + l[0] + '.txt'
    file = open(file_s, 'w+', encoding='utf-8')
    for i in l:
        file.write('\t')
        for ii in i.split('    '):
            file.write(ii)
        file.write('\n')

setDoc(setSrr(url))

#开始自加数值；读取新文档；如果没有；那么跳过
''' 最开始设置为1066142，100  '''
def setNum(num,n):
    l = [(num + i) for i in range(n)]
    sl = [str(l[i]) for i in range(len(l))]
    return sl
    
'''自动产生新的url'''
'''第一章的地址http://www.biquge.com/2_2970/2456497.html
最后一张的地址 http://www.biquge.com/2_2970/3230837.html'''
def setNewUrl(sl):
    urls = []
    for x in sl:
        xsr = 'http://www.biquge.com/2_2970/'+ x +'.html'
        urls.append(xsr)
    return urls


def setTxts(urls):
    for url in urls:
        setDoc(setSrr(url))
    
print(
'''
--------------
开始下载
--------------
'''
)
setTxts(setNewUrl(setNum(2456497,100000)))