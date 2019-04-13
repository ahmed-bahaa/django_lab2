from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from book.models import Book
from .models import Author
# Create your views here.


def show(request,value):
    
    bs= Book.objects.filter(author_id=value)
    adetails = Author.objects.filter(id=value)
    context = { 'books' : bs , 'author': adetails}
    return render(request, 'author/index.html' , context)
    # return HttpResponse(bs)

    # return HttpResponse("hello")
    # 
