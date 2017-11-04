#!/usr/bin/env python3
# _*_ coding = utf-8 _*_

import pymysql

config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'',
    'db':'pythonsql',
    'charset':'utf8'
}
conn = pymysql.connect(**config)
cursor = conn.cursor()
print(conn)
print(cursor)

cursor.close()
conn.close()