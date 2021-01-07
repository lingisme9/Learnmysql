# !/usr/bin/env python
# _*_ coding:utf-8 _*_

# 增加数据 刘德华 56 男 数据到  数据库goods--中students表中
# 修改数据 小王 的名字为 小王吧  数据库goods--中students表中
# 删除数据 李磊               数据库goods--中students表中

# 1.导包
import pymysql

# 2.连接mysql服务端
connc = pymysql.Connect(
    host='192.168.90.172',
    user='root',
    password="mysql",
    database='goods',
    port=3306,
    charset='utf8'
)

# 3.创建游标对象
cur = connc.cursor()

try:
    # 4.编写增加,修改,删除的sql语句
    # 增加数据 刘德华 56 男
    # sql = 'insert into students values(%s,%s,%s,%s)'
    # add_data = [0, '刘德华', 56, '男']

    # 修改数据 小王 的名字为 小王吧
    # sql = 'update students set name=%s where name="小王"'
    # update_data = ['小王吧']

    # 删除数据 李磊
    sql = 'delete from students where name=%s'
    del_data = ['李磊']

    # 5.使用游标对象执行SQL
    cur.execute(sql, del_data)

    # 6.提交操作
    connc.commit()
except Exception as e:
    print(e)
    # 数据回滚
    connc.rollback()
finally:
    # 7.关闭游标对象
    cur.close()
    # 8.关闭连接
    connc.close()

print('game over!')
