import requests

from bs4 import BeautifulSoup

url = "http://www.qq.com/"

wbdata = requests.get(url).text

soup = BeautifulSoup(wbdata,'html.parser')

news_titles = soup.select("div.text > em.f14 > a.linkto")

print(soup)

for n in news_titles:

	title = n.get_text()

	link = n.get("href")

	data = {

		'标题':title,

		'链接':link

	}

	print (data)