# -*- coding:utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from mysite.views import current_time, hours_ahead

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^time/$', current_time),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
]