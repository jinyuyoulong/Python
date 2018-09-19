# coding=utf-8
import urllib2
url = "https://www.baidu.com"
print "第二种方法 带参数"

request = urllib2.Request(url)
request.add_data('a','1')
request.add_header('User-Agent', 'Mozilla/5.0')
response = urllib2.urlopen(request)
print response.getcode()
print len(response.read())
