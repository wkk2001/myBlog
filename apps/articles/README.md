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


a.在apps中注册'markdownx',
    'django.forms',
    'django.contrib.sites',
    'django_comments',
]......等参数
再将STATIC_ROOT = os.path.join(BASE_DIR,'static')注册，运行python manage.py  collectstatic
将markdownx中的css样式放入到static文件夹中
b.在index.html，single_article.html中执行参数的转化，实行调用，最后完成搜索，评论，分页，图标，标签，目录，跳转等功能。
8 实现在虚拟机中的部署情况
a  利用1. yum -y install  gcc  gcc-c++   编译的时候
2. yum -y install wget   
3. yum -y install zlib zlib-devel  openssl  openssl-devel ncurses-devel sqlite sqlite-devel bzip2-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
4. yum -y install epel-release
5. yum -y install libffi-devel  编译Python时候，如果缺少，会导致pip安装不成功
6. yum install psmisc  帮助管理/proc目录，fuser，killall,pstree等
将系统环境的配置完成。
b 源代码中安装Python3.7.4，安装django，uwsgi，进行项目初始化
1. cd /opt  进入opt目录

2. 使用wget命令下载压缩包 wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz

3. tar -zxvf Python-3.7.4.tgz

4. cd Python-3.7.4 

5. ./configure --prefix=/usr/local/python3

6. make 

7. make install

8. 创建软链接
   ln -s /usr/local/python3/bin/python3 /usr/bin/python3
   如果建立错了，删除软连接  rm -rf  /usr/bin/python3

   ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3

9. 给python3安装django
   pip3   install   django
   建立软连接
   ln   -s   /usr/local/python3/bin/django-admin   /usr/bin/django-admin

10. 出错：SQLite 3.8.3 or later is required (found 3.7.17)(执行python3 manage.py makemigtations)
    参考：https://blog.csdn.net/qq_39969226/article/details/92218635
    wget https://www.sqlite.org/2020/sqlite-autoconf-3340000.tar.gz

11. 关闭防火墙: 查看防火墙状态firewall-cmd --state   
    systemctl stop firewalld.service  停止防火墙
    systemctl disable firewalld.service 禁止firewall开机启动 

12. 从网站https://uwsgi-docs.readthedocs.io/en/latest/Download.html下载最新版uwsgi，下载Stable/LTS版本的源文件

13. tar -zxvf uwsgi压缩包文件

14. cd uwsgi解压过的目录

15. python3 setup.py install

16. ln   -s  /usr/local/python3/bin/uwsgi       /usr/bin/uwsgi  建立软连接

17. 安装完成后，使用uwsgi运行
c  安装配置nginx ，配置uwsgi
1. yum -y install nginx  启动nginx：nginx

2. 将server_name 改成自己ip地址

3. 配置location

   ```
   include  uwsgi_params;
   uwsgi_pass  127.0.0.1:8000; 
   ```

4. 在location下新建另一个新的location

   location /static {

   alias /root/www/unicom/static;  //改成你自己的

   }

5. 在manage.py的同级目录下，新建一个uwsgi.ini文件，配置此文件

 ```
   [uwsgi]
   chdir = /home/feixue/python/www/for_test //项目根目录
   module = for_test.wsgi:application //指定wsgi模块
   socket = 127.0.0.1:8000 //对本机8000端口提供服务
   master = true         //主进程
   env = "/opt/myBlog/env"
   #vhost = true          //多站模式
   #no-site = true        //多站模式时不设置入口模块和文件
   #workers = 2           //子进程数
   #reload-mercy = 10
   #vacuum = true         //退出、重启时清理文件
   #max-requests = 1000
   #limit-as = 512
   #buffer-size = 30000
   #pidfile = /var/run/uwsgi9090.pid    //pid文件，用于下脚本启动、停止该进程
   daemonize = /home/feixue/python/www/for_test/run.log    // 日志文件
   disable-logging = true   //不记录正常信息，只记录错误信息
 ```

6. 进入项目目录下，启动服务:uwsgi uwsgi.ini

7. 将settings.py中ALLOWED_HOSTS = ['自己的ip']  
   DEBUG = False

8. 重新运行服务:先删除之前uwsgi进程：killall -9 uwsgi

9. 再次启动 uwsgi uwsgi.ini

10. 启动Django项目,如果出现Error:That port is already in use.   关掉8000的进程就好 sudo fuser -k 8000/tcp·····

d  创建管理员账号 python3 manage.py createsuperuser
e 配置静态资源
1. 打开django项目中settings.py文件（/unicom/settings.py），添加 STATIC_ROOT = ‘/root/www/unicom/static/’
2. 运行python3 manage.py collectstatic，此命令是搜集静态文件的命令，搜集后的静态文件存放在/root/www/unicom/static/中
3. 重新启动uwsgi和nginx。   nginx -s reload      uwsgi uwsgi.ini
4. 配置templates中的 DIRS:[os.path.join(BASE_DIR,'templates')]

f  centos7 安装pipenv
1. pip3 install pipenv
2. 建立软连接   ln -s /usr/local/python3/bin/pipenv /usr/bin/pipenv
3. 创建虚拟环境   pipenv --python 3.7  
4. 虚拟环境地址：/root/.local/share/virtualenvs/bwitclub-kOFaVq63
5. 回到自己项目文件夹，安装具体的库就可以了，pipenv install django
g  cookiecutter 生成bwitclub
1. 回到root目录下
2. cookiecutter https://github.com/pydanny/cookiecutter-django.git
3. 按照提示一顿操作
4. cd bwitclub下
5. pipenv --python 3.7  创建本项目的虚拟环境

剩余的配置！！

## 三、配置pycharm远程连接

1. 配置deployment

​        1.1 Mapping  本地和远程项目目录映射关系

​        1.2 root path 和 deployment path 要等于远程的项目路径

​        1.3 Excluded Paths  添加一些不需要同步到远程的路径，或者不需要下载到本地的路径

2. 连接到服务器上的Python解释器

   

3. 配置Django服务器

   Host  0.0.0.0

   将来运行时候，访问服务器IP



## 四、mysql8和数据库用户设置

1. create database bwitclub charset utf8;  创建主数据库
2. 创建测试数据库 ：create database test_bwitclub charset utf8;
3. 创建bwitclub账户，开发阶段可以设置所有的ip都能访问：create user 'bwitclub'@'%' identified by '12345678';
4. 授权bwitclub账号拥有bwitclub数据库全部的权限：grant all on bwitclub.* to 'bwitclub'@'%';
5. 授权bwitclub账号拥有test_bwitclub数据库全部的额权限：grant all on test_bwitclub.* to 'bwitclub'@'%';
6. 更新权限  ：flush privileges；

## 五、修改项目目录

1. config  配置文件夹

   包括settings的配置，路由配置，wsgi服务器的配置

2. docs 文档目录，因为后续自己写文档，所以清空一下

3. locale  国际化相关的，python manage.py makemessages  给你翻译成对应语言

4. requirements  项目依赖的包

5. utility  本项目需要的脚本和工具，因为系统环境需要自己安装和配置，所以清空一下

6. bwitclub 下的contrib  数据库

7. bwitclub下的 static  ，sass，less  动态化的css 

8. users 应用：已经完成了登录注册找回密码这些功能，adapters.py 将来用于继承django-allauth第三方登录

9. conftest.py ，用pytest测试时候使用的文件

10. .editorconfig    编辑器相关的配置

11. .pylintrc     检查代码是否符合PEP8规范



## 六、安装依赖，运行项目

1. 修改base.txt

   django == 2.2.13 

   连接数据库的引擎  mysqlclient==2.0.1

2. 修改production.txt

   ```python
   # 注释掉
   django-anymail==7.2.1  # https://github.com/anymail/django-anymail
   ```

3. 修改Pipfile的安装源

   ```python
   url = "https://mirrors.aliyun.com/pypi/simple/"
   ```

4. 安装本地运行环境的依赖： pipenv install -r requirements/local.txt





## 七、settings配置

1. base.py

   ```python
   # 设置找到文件路径，也就是最外层的bwitclub，使用的是django-environ
   ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
   
   # 开发过程中使用本地的 .env文件配置
   READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
   
   # 时区和编码语言
   TIME_ZONE = "Asia/Shanghai"
   LANGUAGE_CODE = "zh-Hans"
   
   # 是否将mysql的http请求封装成事务
   DATABASES["default"]["ATOMIC_REQUESTS"] = True
   
   # 打开humanize
   "django.contrib.humanize"
   
   # 暂时不写后台，去掉 "django.contrib.admin",
   
   # 改为False
   CSRF_COOKIE_HTTPONLY = False
   
   # 发送邮件配置，从 .env 文件中读取的配置
   EMAIL_HOST = env('DJANGO_EMAIL_HOST')
   EMAIL_USE_SSL = env('DJANGO_EMAIL_USE_SSL',default=True)
   EMAIL_PORT = env('DJANGO_EMAIL_PORT',default=25)
   EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD')
   DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL')
   
   # 去掉后台管理的配置
   # ADMIN
   # ------------------------------------------------------------------------------
   # Django Admin URL.
   ADMIN_URL = "admin/"
   # https://docs.djangoproject.com/en/dev/ref/settings/#admins
   ADMINS = [("""Bruce""", "bruce@example.com")]
   # https://docs.djangoproject.com/en/dev/ref/settings/#managers
   MANAGERS = ADMINS
   
   # 修改celery的配置
   CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
   # 指定接收的内容类型，增加msgpack数据类型,它比json的序列化更小更快
   CELERY_ACCEPT_CONTENT = ["json","msgpack"]
   # 任务序列化与反序列化使用msgpack，msgpack是一个二进制的json序列化方案
   CELERY_TASK_SERIALIZER = "msgpack"
   # 读取任务一般性能要求不高，使用可读性更好的json就可以
   CELERY_RESULT_SERIALIZER = "json"
   # 单个任务的最大运行时间为5分钟
   CELERY_TASK_TIME_LIMIT = 5 * 60
   # 任务的软时间限制，超时会抛出SoftTimeLimitExceeded异常
   CELERY_TASK_SOFT_TIME_LIMIT = 60
   ```

2. local.py

   ```python
   ALLOWED_HOSTS = ["*"]
   
   
   ```

3. production.py

   ```python
   admin
   email
   media
   static
   Anymail
   这几个部分全部删除
   ```

   

4. .env

   ```python
   #MySQL
   DATABASE_URL=mysql://root:12345678@127.0.0.1/bwitclub
   #REDIS
   REDIS_URL=redis://127.0.0.1:6379
   
   DJANGO_DEBUG=True
   DJANGO_SECRET_KEY=fp2#2%p3z-(g+f--k&0gutlah85vd6wp^y6lc3wfdrkr*l3n_v
   
   #Email
   DJANGO_EMAIL_USE_SSL=True
   DJANGO_EMAIL_HOST=smtp.qq.com
   DJANGO_EMAIL_PORT=25
   DJANGO_EMAIL_HOST_USER=1046244623@qq.com
   DJANGO_EMAIL_HOST_PASSWORD=qucjfwnyidpobbaj
   DJANGO_DEFAULT_FROM_EMAIL=1046244623@qq.com
   #Celery
   CELERY_BROKER_URL=redis://127.0.0.1:6379/1
   CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/2
   ```

5. wsgi.py

   ```python
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
   ```

   

6. 找到users下的admin.py，删除

7. 项目总的urls.py（config下），删除admin相关的路由

8. 去虚拟环境中同步数据库：pipenv run python manage.py migrate，运行项目





## 八、用户模型类 models.py

1. 自定义用户模型

   ```python
   """自定义用户模型"""
   nickname = models.CharField(null=True,blank=True, max_length=255,verbose_name='昵称')
   job_title = models.CharField(max_length=50,null=True,blank=True,verbose_name='职称')
   introduction = models.TextField(blank=True,null=True,verbose_name='简介')
   avatar = models.ImageField(upload_to='user_avatars/',null=True,blank=True,verbose_name='用户头像')
   location = models.CharField(max_length=50,null=True,blank=True,verbose_name='城市')
   personal_url = models.URLField(max_length=255,null=True,blank=True,verbose_name='个人链接')
   weibo = models.URLField(max_length=255, null=True, blank=True, verbose_name='微博链接')
   zhihu = models.URLField(max_length=255, null=True, blank=True, verbose_name='知乎链接')
   github = models.URLField(max_length=255, null=True, blank=True, verbose_name='github链接')
   linkedin = models.URLField(max_length=255, null=True, blank=True, verbose_name='领英链接')
   created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
   update_at = models.DateTimeField(auto_now=True,verbose_name='更新时间')
   
   # 定义元数据
       class Meta:
           verbose_name = '用户'
           verbose_name_plural = verbose_name
           
   # 定义直观读取usename的方法
       def __str__(self):
           return self.username
       
   # nickname不存在就返回username
       def get_profile_name(self):
           if self.nickname:
               return self.nickname
           return self.username
   ```

2. AbstractUser

   ```python
   email = models.EmailField(_('email address'), blank=True)
   # 可以不用写create_at 和 updated_at ,但是为了做到统一就填上了
   date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
   ```

   

3. 设置项目兼容Python2.x版本

   ```python
   from __future__ import unicode_literals
   
   from django.utils.encoding import python_2_unicode_compatible
   
   @python_2_unicode_compatible
   class User(AbstractUser):
   ```

4. 同步数据库

   ```python
   1. pipenv run python manage.py makemigrations
   
   You are trying to add the field 'created_at' with 'auto_now_add=True' to user without a default; the database needs something to populate existing rows.
   
    1) Provide a one-off default now (will be set on all existing rows)
    2) Quit, and let me add a default in models.py
   Select an option: 1     # 输入1，提供当前时间
   Please enter the default value now, as valid Python
   You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
   The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
   Type 'exit' to exit this prompt
   [default: timezone.now] >>>      #直接回车
   
   
   
   2. pipenv run python manage.py migrate
   ```





## 九、第三方登录

1. Django-Allauth             3days ago   star : 5700

   ```python
   文档地址：https://django-allauth.readthedocs.io/en/latest/
   ```

   

2. Django Social Auth     7 years ago   star ：2600

3. Python-Social-Auth   4 years ago    star: 2800



## 十、修改bwitclub

```python
# 安装sorl-thumbnail
pipenv install sorl-thumbnail
在base.py 第三方Apps 'sorl.thumbnail',

# config/urls.py
path("", TemplateView.as_view(template_name="base.html"), name="home"),

# 报错后，将href改为#
<li class="nav-item"><a class="nav-link" href="#">&nbsp;&nbsp;首页</a></li>
```



## 十一、集成第三方账号，github为例

```python
# 第一步
# base.py
THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "django_celery_beat",
    'sorl.thumbnail',
]

# 第二步，github上获取Client ID和Client Secret
settings下的Developer settings  下的 OAuth Apps
地址：https://github.com/settings/developers
  
Client ID
4c62a239f66f5be85d87
Client Secret
644929ac62a5d762b13b405628548fb29bd5546b

# 第三步
socialaccount_socialapp 数据库中增加一条记录
1	GitHub	GitHub	4c62a239f66f5be85d87	644929ac62a5d762b13b405628548fb29bd5546b	
socialaccount_socialapp_sites 数据库中增加一条记录
1	1	1
```

