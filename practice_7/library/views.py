from django.shortcuts import render_to_response
from django.template import Template, RequestContext

from control_panel.library.models import Book
from control_panel.library.models import Author

from django.views.generic import ListView
from django.views.generic import DetailView


class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = "book.html"


class AuthorList(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = "author_card.html"


class BooksDetail(DetailView):
    model = Book
    context_object_name = 'books'
    template_name = "book_list.html"


class AuthorsDetail(DetailView):
    model = Author
    context_object_name = 'authors'
    template_name = "author_list.html"
