#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import os

# 目标链接
url = 'http://www.mzitu.com/page/'
parser = 'html.parser'
cur_path = os.getcwd() + '/'

# 设置请求头
header = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}

preview_page_cnt = 2
for cur_page in range(1, int(preview_page_cnt) + 1):
    cur_url = url + str(cur_page)
    cur_page = requests.get(cur_url, headers = header)
    # 解析网页
    soup = BeautifulSoup(cur_page.text, parser)
    preview_link_list = soup.find(id='pins').find_all('a', target='_blank')[1::2]
    for link in preview_link_list:
        dir_name = link.get_text().strip().replace('?', '')
        link = link['href']
        soup = BeautifulSoup(requests.get(link).text, parser) 

        # 获取图片数量
        pic_cnt = soup.find('div', class_='pagenavi').find_all('a')[4].get_text()
        # 创建目录
        pic_path = cur_path + dir_name
        if os.path.exists(pic_path):
            print('directory exist!')
        else:
            os.mkdir(pic_path)

        # 进入目录，开始下载
        os.chdir(pic_path)
        print('start ' + dir_name + 'loading...')

        # 遍历获取每页图片地址
        for pic_index in range(1, int(pic_cnt) + 1):
            pic_link = link + '/' + str(pic_index)
            cur_page = requests.get(pic_link, headers = header)
            soup = BeautifulSoup(cur_page.text, parser)
            if any(soup):
                pic_src = soup.find('div', 'main-image').find('img')['src']
                pic_name = pic_src.split('/')[-1]
                f = open(pic_name, 'wb')
                f.write(requests.get(pic_src, headers=header).content)
                f.close()
            else:
                print('url is null')
        # 完成下载，退出目录
        os.chdir(cur_path)

print('下载完成')