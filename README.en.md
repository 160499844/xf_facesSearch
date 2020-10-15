# 人脸检索应用程序

#### 介绍
基于face_recognition的人脸检索程序,使用b/s模式交互
1.需要根据人脸库创建npy缓存文件
2.启动项目会初始化npy缓存文件
3.打开项目人脸上传页面，上传图片，进行识别




#### 软件架构
软件架构说明
django
face_recognition


#### 使用说明
1.  需安装好python3环境,把python安装环境添加到path变量中
2.  在项目根目录,即包含manage.py的目录打开cmd,输入python manage.py makemigrations 和 python manage.py migrate 初始化数据库
3.  然后输入python manage.py runserver 8000启动项目
4.  浏览器输入http://127.0.0.1:8000/static/html/faces.html访问


#### 参与贡献

1.  小峰

