import urllib3
import json
import re
import string

of = open('city.json','r')
page = of.read()
of.close()

key = input('请输入要查询天气的城市名： ')
r = '''"市名": "%s",
                    "编码": "(.+?)"''' %key
s = re.findall(r,page,re.S)
s = s[0]

#API更新，旧API时间错误注释掉
#url ='http://m.weather.com.cn/data/%s.html' %s
url ='http://m.weather.com.cn/atad/%s.html' %s
print(url)
http = urllib3.PoolManager()
response = http.request('GET',url)
print(response.data.decode('utf-8'))
we = json.loads(response.data.decode('utf-8'))
print(we)
# print we['city'] , we['date_y'].center(30) ,   we['week']
# print we['temp1'], we['weather1'].center(30),  we['wind1']
# print we['temp2'], we['weather2'].center(30),  we['wind2']
# print we['temp3'], we['weather3'].center(30),  we['wind3']
# print we['temp4'], we['weather4'].center(30),  we['wind4']
# print we['temp5'], we['weather5'].center(30),  we['wind5']
# print we['temp6'], we['weather6'].center(30),  we['wind6']
# print we['index48_d']
# raw_input('plese input anykey to esc')
