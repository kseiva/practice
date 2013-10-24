from django.shortcuts import render_to_response
from django.template import Template, RequestContext

from control_panel.library.models import Book

def book(request):
	books = Book.objects.all()
	return render_to_response('book_list.html', {'books': books},)

def book_list(request, book):
	books = Book.objects.all()
	return render_to_response('book_list.html', {'books': books},)
