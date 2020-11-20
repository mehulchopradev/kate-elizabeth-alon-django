from django.contrib import admin
from .models import Book, PublicationHouse, Review

class ReviewInlineModel(admin.TabularInline):
    model = Review
    min_num = 1
    extra = 1

class BookAdminModel(admin.ModelAdmin):
    list_display = ('title', 'price', 'pages', 'publication_house')
    fields = ('title', 'no_of_copies', 'pages', 'price', 'published_date', 'publication_house')
    search_fields = ('title', 'price')
    list_filter = ('price', 'pages')
    inlines = (ReviewInlineModel,)

class PublicationHouseAdminModel(admin.ModelAdmin):
    list_display = ('name', 'ratings')

# Register your models here.
admin.site.register(Book, BookAdminModel)
admin.site.register(PublicationHouse, PublicationHouseAdminModel)