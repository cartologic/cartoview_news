from django.conf.urls import patterns, url

from . import views, APP_NAME

urlpatterns = patterns('',
                       # app urls
                       url(r'^new/$', views.create, name='%s.new' % APP_NAME),
                       url(r'^list/$', views.list_news, name='%s.list' % APP_NAME),
                       url(r'^read/(?P<news_id>\d+)$', views.details, name='%s.details' % APP_NAME),
                       url(r'^update/(?P<news_id>\d+)$', views.edit, name='%s.edit' % APP_NAME),
                       url(r'^delete/(?P<news_id>\d+)$', views.delete, name='%s.delete' % APP_NAME),
                       )
