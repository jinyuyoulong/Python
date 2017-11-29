# coding=utf-8
import urllib2
url = "https://www.baidu.com"
print '第一种方法'
#直接请求
response = urllib2.urlopen(url)
print (response.getcode())
print (len(response.read()))
