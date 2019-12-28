Django学习记录
--

# Django基础(一)

[虚拟环境与Hello Django](https://mp.weixin.qq.com/s?__biz=MzU4OTgyMDg1OA==&mid=2247483785&idx=1&sn=a1eeab6c66bf30492a013e96937e7602&chksm=fdc6e75ccab16e4a8a56c5aa1d353c86a4c45de62210e1b797de66fe906bb30911f25680c0e0&scene=21#wechat_redirect)

[手写接口与响应](https://mp.weixin.qq.com/s?__biz=MzU4OTgyMDg1OA==&mid=2247483787&idx=1&sn=12b22654936ee04fd47ffa1133b9f81b&chksm=fdc6e75ecab16e4826a54439b54c682dffd30355abce397f15793004db00852a32a150fa8073&token=473567523&lang=zh_CN#rd)

## 一、项目结构
  - DjangoDev03 是项目名
  - 和项目名同名的目录存放Django的相关配置文件
  - DjangoDev03/asgi.py ASGI异步服务器的相关配置
  - DjangoDev03/settings.py 存放是Django全局配置信息
  - DjangoDev03/urls.py 存放全局路由表
  - DjangoDev03/wsgi.py 在部署Django项目时, 使用的wsgi服务器配置信息
  - db.sqlite3 Django默认使用的sqlite文本数据库
  - manage.py Django提供的命令行操作工具, 开发阶段使用它来启动项目和数据库的迁移等等

## 二、创建一个功能应用模块

①先创建子应用
   
#### 子应用意义:
- 往往是Django最小功能模块， 会以应用写形式呈现
- 方便重用
- 结构更清晰

#### 子应用结构
- projects/migrations 存放数据库迁移的相关信息
- projects/admin.py 为admin站点的配置信息
- projects/apps.py 存放的是app的标签等相关信息
- projects/models.py 存放数据库模型相关信息
- projects/tests.py 存放的当前应用单元测试相关信息
- projects/views.py 主要定义相关功能（业务逻辑）
    
②在DjangoDev03/settings.py全局配置文件中的, INSTALLED_APPS列表中添加app的信息
   
③在projects/views.py中, 来创建相关功能(视图函数)
   
④在DjangoDev03/urls.py全局路由表中, 添加路由信息

