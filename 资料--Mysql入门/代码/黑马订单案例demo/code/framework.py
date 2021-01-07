"""web框架的职责专门负责处理动态资源请求"""
import time
import json
import logging
import pymysql


# 封装一个执行crud的函数
def execut_crud_sql(sql, data):
    # 2.连接mysql的服务端
    conc = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        database='orders',
        charset='utf8'
    )

    # 3.创建游标对象
    cur = conc.cursor()

    try:

        # 4.编写增加 数据的流程 SQL 语句
        # 5.使用游标对象 执行 SQL 语句
        cur.execute(sql, data)

        # 6.提交操作
        conc.commit()
    except Exception as e:
        print('操作失败:', e)
        # 回滚数据
        conc.rollback()
    finally:

        # 关闭游标
        cur.close()

        # 关闭连接
        conc.close()


# 1.获取订单数据展示
def order(body):
    # 2.链接mysql的服务端
    conc = pymysql.Connect(
        host='127.0.0.1',
        user='root',
        password="root",
        database='orders',
        port=3306,
        charset='utf8'
    )

    # 3.创建游标对象
    cur = conc.cursor()

    try:
        # 4.编写 查询orders表的 所有数据 SQL
        sql = 'select * from orders;'
        # 5.使用 游标对象 执行 SQL
        cur.execute(sql)

        # 6.获取查询的所有结果 fetchall()==>元祖
        result = cur.fetchall()
        # print("查询数据:",result)

        # 7.将数据 转换成 [{},{}]
        data_list = []
        for row in result:
            data_list.append({
                #  id | count | price  | freight | user   | status    | time
                'id': row[0],
                'count': row[1],
                'price': str(row[2]),
                'freight': str(row[3]),
                'user': row[4],
                'status': row[5],
                'time': str(row[6]),

            })

    # 8.加个try 优化下
    # print('查询:',data_list)
    except Exception as e:
        print('报错信息:', e)
    finally:
        # 关闭游标对象
        cur.close()
        # 关闭连接
        conc.close()

    # 把列表转成json字符串数据
    # ensure_ascii=False 表示在控制台能够显示中文
    json_str = json.dumps(data_list, ensure_ascii=False)

    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [
        ("Server", "PWS/1.1"),
        # 指定编码格式，因为没有模板文件，可以通过响应头指定编码格式
        ("Content-Type", "text/html;charset=utf-8")
    ]
    return status, response_header, json_str


# 2.增加订单数据
def add(body):
    # 执行增加的sql语句
    sql = 'insert into orders values(%s,%s,%s,%s,%s,%s,%s)'
    execut_crud_sql(sql, body)

    json_str = json.dumps({'data': "增加成功！"}, ensure_ascii=False)
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [
        ("Server", "PWS/1.1"),
        # 指定编码格式，因为没有模板文件，可以通过响应头指定编码格式
        ("Content-Type", "text/html;charset=utf-8")
    ]
    return status, response_header, json_str


# 3.修改订单数据
def update(body):
    print('修改的数据:', body)
    # ['7', '99', '9.90', '1.00', '明明', '待收货', '2020-03-29']

    body.append(body.pop(0))

    # 1.修改的 sql语句 id | count | price  | freight | user      | status    | time
    sql = 'update orders set count=%s,price=%s,freight=%s,user=%s,status=%s,time=%s where id=%s'

    # 2.调用执行
    execut_crud_sql(sql, body)

    json_str = json.dumps({'data': "修改成功！"}, ensure_ascii=False)

    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [
        ("Server", "PWS/1.1"),
        # 指定编码格式，因为没有模板文件，可以通过响应头指定编码格式
        ("Content-Type", "text/html;charset=utf-8")
    ]
    return status, response_header, json_str


# 4.删除订单数据
def delete(body):
    print('删除的数据:', body)

    # 1.sql语句 删除
    sql = 'delete from orders where id=%s'

    # 2.执行
    execut_crud_sql(sql, body)

    json_str = json.dumps({'data': "删除成功！"}, ensure_ascii=False)

    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [
        ("Server", "PWS/1.1"),
        # 指定编码格式，因为没有模板文件，可以通过响应头指定编码格式
        ("Content-Type", "text/html;charset=utf-8")
    ]
    return status, response_header, json_str


# index.html展示
def index(body):
    # 状态信息
    status = "200 OK"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]
    # 1. 打开指定模板文件，读取模板文件中的数据
    with open("./static/index.html", "r",encoding = 'UTF-8') as file:
        file_data = file.read()

    # 这里返回的是元组
    return status, response_header, file_data


# 处理没有找到的动态资源
def not_found():
    # 状态信息
    status = "404 Not Found"
    # 响应头信息
    response_header = [("Server", "PWS/1.1")]
    # web框架处理后的数据
    data = "not found"

    # 这里返回的是元组
    return status, response_header, data


# 路由列表, 列表里面的每一条记录都是一个路由
route_list = [
    # 首页显示
    ('/index.html', index),
    # 1.获取所有订单url
    ("/orders.html", order),
    # 2.增加订单url
    ("/add_order.html", add),
    # 3.修改订单url
    ("/update_order.html", update),
    # 4.删除订单url
    ("/delete_order.html", delete),
]


# 处理动态资源请求f
def handle_request(env):
    # 获取动态的请求资源路径
    request_path = env["request_path"]
    print("动态资源请求的地址:", request_path)
    body = env.get('body')
    # 遍历路由列表，匹配请求的url
    for path, func in route_list:
        if request_path == path:
            # 找到了指定路由，执行对应的处理函数
            result = func(body)
            return result
    else:
        # 没有动态资源数据, 返回404状态信息
        result = not_found()
        logging.error("没有设置相关的路由信息:" + request_path)
        # 把处理后的结果返回给web服务器使用，让web服务器拼接响应报文时使用
        return result
