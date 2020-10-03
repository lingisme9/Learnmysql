# Mysql

## 一、安装

### 1.下载地址

​		win10可以下载msi，大的是离线安装，小的是在线安装

```
https://dev.mysql.com/downloads/mysql/
```

### 2.第一种安装方式zip

+ 下载解压zip到指定路径

+ mysql根目录配置my.ini

  ```
  [mysqld]
  # 设置3306端口
  port=3306
  # 设置mysql的安装目录
  basedir=D:\\Mysql\\mysql-8.0.19-winx64
  # 设置mysql数据库的数据的存放目录
  datadir=D:\\Mysql\\mysql-8.0.19-winx64\\data   
  # 允许最大连接数
  max_connections=200
  # 允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统
  max_connect_errors=10
  # 服务端使用的字符集默认为UTF8
  character-set-server=utf8
  # 创建新表时将使用的默认存储引擎
  default-storage-engine=INNODB
  # 默认使用“mysql_native_password”插件认证
  default_authentication_plugin=mysql_native_password
  [mysql]
  # 设置mysql客户端默认字符集
  default-character-set=utf8
  [client]
  # 设置mysql客户端连接服务端时默认使用的端口
  port=3306
  default-character-set=utf8
  ```

  + cmd进入bin目录

    1.生成root初始密码，用于第一次登录

    ​	` mysqld --initialize --console`

    2.安装mysql服务，名字可以自己写

    ​	 `mysqld -install mysql`

    3.开启服务

    ​	`net start mysql`

    4.root登录

    ​	`mysql -u root -p`

    5.更换root密码进去mysql输入

    ​	`ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';`

  + 



+ 设置环境变量 Mysql：bin目录的路径，path也可以添加一个

### 3.第三种msi

跟正常安装其他的一样，基本都是默认选项，不需要配置my.ini

![image-20201004023133933](https://gitee.com/lingisme9/typora/raw/master/img/image-20201004023133933.png)

可视化工具

![image-20201004023214155](https://gitee.com/lingisme9/typora/raw/master/img/image-20201004023214155.png)

### 4.常见问题

![image-20201004023314437](https://gitee.com/lingisme9/typora/raw/master/img/image-20201004023314437.png)

服务正在启动，服务无法启动

**端口占用**

1. mysql启动需要的端口3306，如果被占用了的话就无法启动服务。

   同样的，我们打开CMD，输入命令**netstat -ano，**左边是端口，右边是PID。

   **查看占住3306端口的PID。**

   ![怎么解决mysql服务无法启动的问题？](https://gitee.com/lingisme9/typora/raw/master/img/e57a258602214f57e36e6008732064fb970b738f.jpg)

2. 打开任务管理器，点击详细信息，通过PID找到占用端口的应用，关闭再启动Mysql即可。若是mysql占用，那么就不是端口的原因。

   ![怎么解决mysql服务无法启动的问题？](https://gitee.com/lingisme9/typora/raw/master/img/f9617afb960b312173593710dee983aee9d76d8f.jpg)

**用户设置**

1. 可以通过用户设置修改临时密码的方式解决服务无法启动的问题，在CMD上输入路径进入到bin目录下。

   执行**mysql -uroot，**即可修改密码。

   然后使用密码登录mysql环境。

   ![怎么解决mysql服务无法启动的问题？](https://gitee.com/lingisme9/typora/raw/master/img/05e24be983aee8d72212d05c6b781431deb6668f.jpg)