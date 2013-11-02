from django.contrib import admin
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from control_panel.library.models import Author, Book, Publisher, BooksImage


class ImageInline(generic.GenericTabularInline):
    model = BooksImage


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_display_links = ('first_name', 'last_name', )
    ordering = ('last_name', 'first_name', )


class BookAdmin(admin.ModelAdmin):

    def cov_count(self, img):
        cnt = 0
        for c in BooksImage.objects.filter(id=img.id):
            if c.small_img:
                cnt += 1
            if c.large_img:
                cnt += 1
            return cnt
    cov_count.allow_tags = True

    def cov_view_small_img(self, img):
        link = ""
        for c in BooksImage.objects.filter(id=img.id):
            link = c.view_small_img()
            return link
    cov_view_small_img.allow_tags = True

    def cov_view_large_img(self, img):
        link = ""
        for c in BooksImage.objects.filter(id=img.id):
            link = c.view_large_img()
            return link
    cov_view_large_img.allow_tags = True

    list_display = ('title', 'publisher', 'publication_date', 'cov_count', 'cov_view_small_img', 'cov_view_large_img', )
    list_display_links = ('title', )
    search_fields = ('title', )
    list_filter = ('publication_date', )
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date', )
    filter_horizontal = ('authors', )
    inlines = (ImageInline, )


class PublisherAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Contact info', {
            'classes': ('collapse', ),
            'fields': ('country', 'city', 'address'), }), )
    list_display = ('title', 'country', 'city', )
    list_display_links = ('title', )
    ordering = ('title', )
    list_filter = ('country', 'city', )


class BooksImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'link_book', 'view_small_img', 'view_large_img', )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(BooksImage, BooksImageAdmin)
