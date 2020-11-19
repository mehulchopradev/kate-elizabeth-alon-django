from django.db import models

# Create your models here.
class User(models.Model):
    # id
    username = models.CharField(null=False, blank=False, max_length=20, unique=True)
    password = models.IntegerField(null=False, blank=False)
    gender = models.CharField(null=False, blank=False, max_length=1)
    country = models.CharField(null=True, blank=True, max_length=5)

# 1 publication house can publish many books
# 1 book can be published only by 1 publication house

class PublicationHouse(models.Model):
    # id
    name = models.CharField(null=False, blank=False, max_length=30)
    ratings = models.IntegerField(null=False, blank=False)

class Book(models.Model):
    # id
    title = models.CharField(null=False, blank=False, max_length=30)
    price = models.FloatField(null=True, blank=True)
    pages = models.IntegerField(null=False, blank=False)
    published_date = models.DateField(null=True, blank=True)
    no_of_copies = models.IntegerField(null=False, blank=False)

    publication_house = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
