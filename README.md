## 这是一个Flask入门学习项目
* from: https://read.helloflask.com/

### 准备工作
1. python虚拟环境(需要安装pyenv、pipenv)
> pipenv install --python 3.6 
2. git管理
3. 安装flask
> pipenv install flask

### Hello Flask!
1. 添加.flaskenv设置环境变量
2. 添加app.py设置简单视图函数

### 模板
1. 添加了Templates目录及index.html文件
2. 视图函数使用render_template传入虚拟函数

### 静态文件
1. 新增static目录及图片文件
2. 引用本地图片并加载css文件style.css