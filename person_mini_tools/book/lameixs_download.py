# -*- coding: utf-8 -*-
import re
import urllib.request as request  
from bs4 import BeautifulSoup  
import requests

import lameixs_menu
import lameixs_reader

def main():
    nextURL = 'http://m.lameixs.com/reader/34721/447601.html'
    while nextURL.endswith('.html'):
        content,nextURL = lameixs_reader.getContent(nextURL)
        lameixs_reader.setDoc(content,'火淫忍者系列')
    

    # urls = lameixs_menu.getURLs()
    # for url in urls:
    #     print(url)
    #     content = lameixs_reader.getContent(url)
    #     lameixs_reader.setDoc(content)
    


if __name__ == '__main__':
    main()