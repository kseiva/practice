from django.contrib import admin
from control_panel.library.models import Author, Book, Publisher


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	list_display_links = ('first_name', 'last_name',)
	ordering = ('last_name', 'first_name',)

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date')
	list_display_links = ('title',)
	search_fields = ('title',)
	list_filter = ('publication_date',)
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)
	filter_horizontal = ('authors',)

class PublisherAdmin(admin.ModelAdmin):
	fieldsets = (
	    ('Contact info', { 
		'classes': ('collapse',),
		'fields' : ('country', 'city', 'address'),
		}),
     	)
	list_display = ('title', 'country', 'city')
	list_display_links = ('title',)
	ordering = ('title',)
	list_filter = ('country', 'city',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)

