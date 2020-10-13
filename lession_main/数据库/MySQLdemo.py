#!/usr/bin/python
#coding:utf-8

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="333", db="wordpress")
c = db.cursor()
max_price = 5
c.execute("""SELECT * FROM wp_posts""")
r = c.fetchone()
print(r)

# pip install mysqlclient if py veriosn > 3
# 文件名不能和import的包名一致，不能为 MySQLdb.py 否则会失败 !!!