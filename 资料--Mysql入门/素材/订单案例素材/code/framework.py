"""web框架的职责专门负责处理动态资源请求"""
import time
import json
import logging
import pymysql

# 1.获取订单数据展示
def order(body):

    # 2.链接mysql的服务端

    # 3.创建游标对象

    # 4.编写 查询orders表的 所有数据 SQL

    # 5.使用 游标对象 执行 SQL

    # 6.获取查询的所有结果 fetchall()==>元祖

    # 7.将数据 转换成 [{},{}]

    # 8.加个try 优化下
    
    # 把列表转成json字符串数据
    # ensure_ascii=False 表示在控制台能够显示中文
    json_str = json.dumps([], ensure_ascii=False)

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
    with open("./static/index.html", "r") as file:
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
