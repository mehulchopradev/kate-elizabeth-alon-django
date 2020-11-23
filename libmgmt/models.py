from django.db import models
from datetime import date

# Create your models here.
class User(models.Model):
    # id
    username = models.CharField(null=False, blank=False, max_length=20, unique=True)
    password = models.IntegerField(null=False, blank=False)
    gender = models.CharField(null=False, blank=False, max_length=1)
    country = models.CharField(null=True, blank=True, max_length=5)

# 1 publication house can publish many books
# 1 book can be published only by 1 publication house

# Many to Many
# 1 logged in user can issue many books (1 to *)
# 1 book can be issued to more than one logged in user (1 to *)

class PublicationHouse(models.Model):
    # id
    name = models.CharField(null=False, blank=False, max_length=30)
    ratings = models.IntegerField(null=False, blank=False)

    # book_set

    def __str__(self):
        return self.name

# 1 book can have many reviews
# A review can be given only to a particular book

class Book(models.Model):
    # id
    title = models.CharField(null=False, blank=False, max_length=30)
    price = models.FloatField(null=True, blank=True)
    pages = models.IntegerField(null=False, blank=False)
    published_date = models.DateField(null=True, blank=True)
    no_of_copies = models.IntegerField(null=False, blank=False)

    publication_house = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, through='BooksIssued')

    # review_set

    def __str__(self):
        return self.title

class Review(models.Model):
    # id
    personality_name = models.CharField(null=False, blank=False, max_length=20)
    description = models.CharField(null=False, blank=False, max_length=50)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class BooksIssued(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField(null=False, default=date.today())
    return_date = models.DateField(null=True)
