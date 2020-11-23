from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Book, User, BooksIssued
from datetime import date

def show_landing(request):
    session = request.session
    if 'username' not in session:
        return HttpResponseRedirect(reverse('libapp:home'))
    username = session['username']
    user = User.objects.get(username=username)

    books = Book.objects.order_by('-pages')
    for book in books:
        if book.no_of_copies == 0:
            book.issueable = False # on django model class objects we can set derived properties
        else:
            users = book.users.all()
            book.issueable = True

            if user in users:
                book.can_issue = False # derived property added to the django model object
            else:
                if len(users) == book.no_of_copies:
                    book.issueable = False
                else:
                    book.can_issue = True

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

def issue_book(request, bookId):
    session = request.session
    if 'username' not in session:
        return HttpResponseRedirect(reverse('libapp:home'))
    username = session['username']

    user = User.objects.get(username=username)
    book = Book.objects.get(id=bookId)
    # book.users.add(user)

    book_issued = BooksIssued(book=book, user=user)
    book_issued.save()

    return HttpResponseRedirect(reverse('libapp:landing'))

def return_book(request, bookId):
    session = request.session
    if 'username' not in session:
        return HttpResponseRedirect(reverse('libapp:home'))
    username = session['username']

    user = User.objects.get(username=username)
    book = Book.objects.get(id=bookId)
    # book.users.remove(user)

    books_issued = BooksIssued.objects.get(book=book, user=user)
    books_issued.return_date = date.today()
    books_issued.save()

    return HttpResponseRedirect(reverse('libapp:landing'))
