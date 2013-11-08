from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
import datetime
from django.core.urlresolvers import reverse
from control_panel.settings import MEDIA_ROOT

# Create your models here.
# -*- coding: utf-8 -*-


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(null=True)
    birthyear = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('control_panel.library.views.authors_list', args=[str(self.id)])


class Publisher(models.Model):
    title = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField()

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.title, self.city, self.country)


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(auto_now_add=True)
    description = models.TextField(null=False, blank=False, default="")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('control_panel.library.views.books_info', args=[str(self.id)])


class BooksImage(models.Model):
    small_img = models.ImageField(upload_to=MEDIA_ROOT)
    large_img = models.ImageField(blank=True, null=True, upload_to=MEDIA_ROOT)
    img_id = models.PositiveIntegerField()
    link_book = models.ForeignKey(Book)
    cont_type = models.ForeignKey(ContentType)
    cont_obj = generic.GenericForeignKey("cont_type", "img_id")

    def __unicode__(self):
        return '%s' % self.id

    def img_count(self):
        count = 0
        if self.small_img:
            count += 1
        if self.large_img:
            count += 1
        return '%s' % count

    def view_small_img(self):
        return u'<img src="%s"/>' % (self.small_img.url)
    view_small_img.allow_tags = True

    def view_large_img(self):
        return u'<img src="%s"/>' % (self.large_img.name)
    view_large_img.allow_tags = True
