# -*- coding:utf-8 -*-
# URL配置
from django.conf.urls.default import *
import views

urlpatterns = patterns('',
	(r'^latest/$', views.latest_books),
	)
