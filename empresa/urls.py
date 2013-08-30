# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    ('^hello', views.MyView.as_view()),
)


urlpatterns = patterns('',
    url(r'^criar/$', views.FuncionarioCreateView.as_view(), name='criar'),
    url(r'^atualizar/(?P<pk>\d+)/$',views.FuncionarioUpdateView.as_view(),name='atualizar'),
 )