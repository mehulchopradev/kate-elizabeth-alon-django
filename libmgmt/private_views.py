from django.shortcuts import render
from .models import Book

def show_landing(request):
    books = Book.objects.order_by('-pages')
    data = {
        'books': books
    }
    return render(request, 'libmgmt/private/landing.html', data)