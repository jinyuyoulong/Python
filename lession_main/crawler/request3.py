# coding=utf-8
import urllib2, cookielib
print ('第三种方法 带cookie')

#creat cookie 容器
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
#create a opener
opener = urllib2.build_opener(handler)

#给urllib2安装opener
#urllib2.intall_opener(opener)

response = urllib2.urlopen('http://www.baidu.com')
for item in cookie:
	print 'Name = '+item.name
	print 'Value ='+item.value
#print response.status_code
#print response.read()
print cookie
