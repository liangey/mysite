#Author:ley
# --*-- coding: utf-8 --*--
#@Time : 2019-01-02 15:14
#@Author: ley
#@Site : 
#@File : urls.py
#@Software : PyCharm
from django.urls import path,re_path
from . import views



urlpatterns=[
    re_path(r'^$',views.index,name='index'),
    re_path(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    re_path(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='resulst'),
    re_path(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]