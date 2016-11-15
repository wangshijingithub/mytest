# -*- coding:utf-8 -*-
#业务逻辑层
from django.shortcuts import render
from models import Book

def latest_books(request):
	book_list = Book.objects.order_by('-pub_date')[:10]
	return render(request, 'latest_book.html', {'book_list':book_list})
