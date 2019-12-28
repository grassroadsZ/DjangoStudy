# encoding:utf-8
# Motto：good good study, day day up. why you so lazy ？？？
from django.urls import path

# from projects.views import index
from .views import index

# 子路由(子应用下创建的路由表)
urlpatterns = [
    path('index_page/', index),
]