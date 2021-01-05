1.我的第一个Django项目博客
一、环境配置

VSCode 下载，安装python ，chinese，path intellisence，npm ，npm intellisence ,Vetur，Vue3 Snippets ,vscode-icons，live server 这些插件

配置终端

切换到cmd

安装前端开发工具HbuilderX https://www.dcloud.io/hbuilderx.html

安装小程序开发工具 https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

二、安装git：https://git-scm.com/；

创建远程仓库myBlog

初始化本地仓库，也就是在本地的myBLog文件夹下执行：git init，执行完后会创建一个.git的隐藏文件

远程仓库和本地仓库进行关联：git remote add origin "你的远程仓库地址"

如果出现错误，ssh没有创建

先去创建密钥：ssh-keygen ，一路enter，生成密钥

查看生成的密钥 cat ~/.ssh/id_rsa.pub，将密钥写入到github上的settings下的SSH and GPG keys下

推送四步骤：

git status 查看发生变化的文件

git add . 追踪所有发生变化的文件

git commit -m "备注" 提交到本地仓库

git push -u origin master 第一次提交 到远程仓库

git push 之后的提交

三、创建myBlog项目

空文件夹下，执行 django-admin startproject myBlog;
给myBlog创建虚拟环境，使用：python -m venv env
进入到虚拟环境，windows下：.\\env\\Scrtipst\\activate;
退出虚拟环境，windows下：deactivate；
使用VSCode打开myBlog，执行：python manage.py startapp articles
四、创建articles的models

创建model

数据库同步

在admin.py中注册model




五  业务逻辑

1 文章列表页，分页

2文章详情页，评论

3全局搜索功能

4最新文章，最新评论的排行

5按照分类，标签的一个聚类操作

6联系我页面，发送邮件

6  聚拢到apps文件夹
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR,"apps"))


a:实现标签，实现目录，实现跳转，实现搜索，实现分页，实现图标
7评论集成插件
django-contrib-comments
django-markdownfy