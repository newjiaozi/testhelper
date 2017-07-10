#coding:utf-8
'''
Created on 2016��10��28��

@author: ldl
'''
from django.conf.urls import url
from .views import respBad

urlpatterns = [
    url(r'^',respBad),
#     url(r'^taobao', taobao),
]