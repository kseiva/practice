# ~*~ coding: utf-8 ~*~

from django.conf.urls import patterns, include, url
from control_panel.pages.views import home

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'control_panel.views.home', name='home'),
    # url(r'^control_panel/', include('control_panel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

      url(r'^$', 'control_panel.pages.views.home'),
      url(r'^log/(?P<path>.*)$', 'control_panel.pages.views.listing'),
)
