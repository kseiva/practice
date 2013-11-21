# ~*~ coding: utf-8 ~*~

from django.conf import settings
from django.conf.urls import patterns, include, url
from control_panel.pages.views import home
from control_panel.orders.views import CustomersList
from control_panel.orders.views import CustomerDetails
from control_panel.library.views import BookList, AuthorList, BooksDetail, AuthorsDetail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'control_panel.views.home', name='home'),
    # url(r'^control_panel/', include('control_panel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', 'control_panel.pages.views.home'),
    url(r'^log/(?P<path>.*)$', 'control_panel.pages.views.listing'),
    url(r'^library/$', BookList.as_view()),
    url(r'^library/books/$', BookList.as_view()),
    url(r'^library/books/(?P<pk>\d+)$', BooksDetail.as_view(), name='book_list.html'),
    url(r'^library/authors/(?P<pk>\d+)$', AuthorsDetail.as_view(), name='author_list.html'),
    url(r'^library/authors/$', AuthorList.as_view(), name='author_card.html'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^orders/$', CustomersList.as_view(), name='order_list.html'),
    url(r'^orders_list/(?P<pk>\d+)/$', CustomerDetails.as_view(), name='customer.html'),
    url(r'^registration/$', 'control_panel.registration.views.registrate'),
    url(r'^login/$', 'control_panel.registration.views.log_in'),
    url(r'^admin/', include(admin.site.urls)),
)
