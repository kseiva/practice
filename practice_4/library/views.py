from django.shortcuts import render_to_response
from django.template import Template, RequestContext

from control_panel.library.models import Book
from control_panel.library.models import Author

def book(request):
	books = Book.objects.all()
	return render_to_response('book.html', {'books': books},)

def authors_list(request, author_id):
	authors = Author.objects.get(id=author_id)
	return render_to_response('author_list.html', {'authors': authors},)

def books_info(request, book_id):
	books = Book.objects.get(id=book_id)
	return render_to_response('book_list.html', {'books': books},)

def authors_card(request):
	authors = Author.objects.all()
	return render_to_response('author_card.html', {'authors': authors},)

