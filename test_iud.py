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

sql_insert = "insert into user(userid,username) values(10, 'name10')"
sql_update = "update user set username = 'username91'  where userid = 9"
sql_delete = "delete from user where userd < 3"

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)

    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

cursor.close()
conn.close()