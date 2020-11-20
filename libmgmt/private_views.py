from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Book

def show_landing(request):
    session = request.session
    if 'username' not in session:
        return HttpResponseRedirect(reverse('libapp:home'))
    username = session['username']

    books = Book.objects.order_by('-pages')
    data = {
        'books': books,
        'username': username,
    }
    return render(request, 'libmgmt/private/landing.html', data)

def show_book_details(request, bookId):
    session = request.session
    if 'username' not in session:
        return HttpResponseRedirect(reverse('libapp:home'))
    username = session['username']

    book = Book.objects.get(id=bookId)
    data = {
        'book': book,
        'username': username
    }
    return render(request, 'libmgmt/private/book-details.html', data)

def logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse('libapp:home'))