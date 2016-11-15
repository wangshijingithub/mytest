# -*- coding:utf-8 -*-
#数据表库
from django import models

class Book(models.Model):
	name = models.CharField(max_length=50)
	pub_date = models.DateField()