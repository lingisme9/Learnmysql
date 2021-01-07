# !/usr/bin/env python
# _*_ coding:utf-8 _*_

# 查询 数据库goods--中students的所有数据

# 1.导包
import pymysql

try:
    # 2.连接mysql数据库的服务
    connc = pymysql.Connect(
                # mysql服务端的IP 默认127.0.0.1/localhost-真实IP
                host='192.168.90.172',
                user='root',
                password="mysql",
                database='goods',
                port=3306,
                charset='utf8'
    )

    # 3.创建游标对象
    cur = connc.cursor()

    # 4.编写SQL语句
    sql = 'select * from students;'

    # 5.使用游标对象去调用SQL
    cur.execute(sql)

    # 6.获取查询的结果 --print()
    result = cur.fetchall()
    print(result)

    # 7.关闭游标对象
    cur.close()

    # 8.关闭连接
    connc.close()
except Exception as e:
    print(e)

