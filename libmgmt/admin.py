from django.contrib import admin
from .models import Book

class BookAdminModel(admin.ModelAdmin):
    list_display = ('title', 'price', 'pages')
    fields = ('title', 'no_of_copies', 'pages', 'price', 'published_date')
    search_fields = ('title', 'price')
    list_filter = ('price', 'pages')

# Register your models here.
admin.site.register(Book, BookAdminModel)