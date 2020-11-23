from django.urls import path
from .views import show_home, show_register, register, authenticate, login
from .private_views import show_landing, show_book_details, logout, issue_book, return_book

# lib/

app_name = 'libapp'

urlpatterns = [
    path('home/', login, name='home'),
    path('sign-up/', show_register, name='signup'),
    path('register/', register, name='register'),
    path('auth/', login, name='auth'),
    path('private/landing/', show_landing, name='landing'),
    path('private/book-details/<int:bookId>', show_book_details, name='bookDetails'),
    path('private/logout', logout, name='logout'),
    path('private/issue-book/<int:bookId>', issue_book, name='issueBook'),
    path('private/return-book/<int:bookId>', return_book, name='returnBook')
]
