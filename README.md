## 基于Django+Simpleui的博客系统

前端：[hexo-theme-matery](https://github.com/blinkfox/hexo-theme-matery)
就是我[博客]()的hexo主题

后台：[SimpleUi](https://simpleui.88cto.com/simpleui)

Django：[Django 3.0.5](https://www.djangoproject.com/)       

Python：python3.8

### 假设你已经装好了Python环境 然后项目已经导入到了pycharm

- 打开终端 新建一个虚拟环境
```python
#a：安装虚拟环境
        pip  install virtualenv virtualenvwrapper-win -i https://pypi.douban.com/simple

#b:创建一个虚拟环境
	mkvirtualenv envname     # envname表示虚拟环境的名称,可以自定义

#c：退出虚拟环境
	deactivate 

#d：进入虚拟环境
	workon envname

#e：删除一个虚拟环境
	rmvirtualenv envname

#f：查看当前系统中有哪些虚拟环境
	workon  或者  lsvirtualenv 

```

- 切换到你创建好的虚拟环境变量 检查当前目录是不是项目的根目录
```python
        workon envname
```
- 在虚拟环境中安装项目所需的第三方包

```python
        pip  install  -r requirements.txt  -i https://pypi.douban.com/simple
```
- 切换ide虚拟环境 选择对应的python.exe文件 虚拟环境地址在c盘用户下的Envs中

- 如果是第一次启动项目需要先创建超级管理员
```python
    python manage.py createsuperuser   #创建管理员用户,设置密码
    python manage.py changepassword   #修改管理员用户的密码
```
- 如果是第一次启动项目需要创建网站默认配置
1. 打开根目录中initSql.py文件
2. 右键运行

- 最后在终端中输入 
```python
    python manage.py runserver   #默认端口8000  可以在命令后直接加需要启动的端口

```
- 网址后面加/admin 进入后台  输入你的管理员账户密码即可登录 
- 请优先修改 网站后台 然后网页就不会报错
- 百度和谷歌统计请自行在base.html中修改






























