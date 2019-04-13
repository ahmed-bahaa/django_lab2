from django.db import models
from Author.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    bid = models.AutoField(primary_key=True)
    author_id = models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True, null=True)



class comment(models.Model):
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    cid = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book,on_delete=models.SET_NULL,blank=True, null=True)

