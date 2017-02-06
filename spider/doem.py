# -*- coding: UTF-8 -*-
#!/usr/bin/env python3

str = raw_input()
list = str.split(',')
for i in xrange(0,len(list)):
	item = list[i]
 	for j in xrange(0,len(list)):
 		if j!=i:
 			print item+list[j]