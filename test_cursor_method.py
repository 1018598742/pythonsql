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

sql = 'select * from user'
cu = cursor.execute(sql)
print('cu is:',cu)

print(cursor.rowcount)

rs = cursor.fetchone()
print(rs)

rs = cursor.fetchmany(3)
print(rs)

rs = cursor.fetchall()
print(rs)



cursor.close()
conn.close()