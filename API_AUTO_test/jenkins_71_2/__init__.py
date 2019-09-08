# -*- coding:utf-8 -*-
# @Time : 2019-09-08
# @Author：lqc
# @Email:572948875@qq.com
# File : __init__.py.py


# jenkins是什么？
# jenkins是一个开源的、提供友好操作界面的持续集成(CI)工具，起源于Hudson(Hudson是商用的)，
# 主要用于持续、自动的构建/测试软件项目、监控外部任务的运行，Jenkins用Java语言编写，可在Tomcat
# 等流行的servlet容器中运行，也可独立运行。
# 通常与版本管理工具(SCM)、构建工具结合使用；常用的版本控制工具有svn、GIT,构建工具有Maven、Ant、Gradle

# 它在我们的项目中有什么实际的使用？
# 部署测试环境
# 跑定时任务(结合自动化/测试工具可以使用)

# Jenkins+自动化
# Jenkins+ant
# Jenkins+ant+jemter

# 安装Jekins&Jekins的使用介绍
# 1、Windows版本：
#    直接利用Windows安装包进行一键式安装即可。安装完了之后打开地址：http://localhost:8080/ 记得设置为服务
# 2、linux+tomcat版本：
#    上传war包到tomcat下的webapps
#    启动tomcat-bin下面，输入./startup.sh
#    安装jenkins-->输入地址：ip地址：8080/jenkins
#    安装之前会看到下面的输入密码的界面
#    你会看到这个界面，告诉你要进行输入密码，利用命令 cat /root/.jenkins/secrets/initialAdminPassword获取到密码，填入，点击下一步即可

# 学习目标：
# 1、安装Jenkins&Jenkins
