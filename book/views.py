from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from book.models import Book,comment
from .forms import AddCommentForm
# Create your views here.


def index(request):
    bs= Book.objects.all()
    context = { 'books' : bs}
    return render(request, 'book/index.html' , context )


def book_details(request,id):
    form = AddCommentForm(request.POST)
    book_ref= Book.objects.get(bid=id)
    if request.method=='POST':    
        if form.is_valid():
                com = comment(title=request.POST['title'] , email=request.POST['email'] ,book=book_ref)
                com.save()
                comments = comment.objects.filter(book=book_ref)
                context = { 'book' : book_ref ,'comments':comments ,'form': form}
                return render(request, 'book/details.html' , context)
    else:    
        form = AddCommentForm()    
        comments = comment.objects.filter(book=book_ref)
        context = { 'book' : book_ref ,'comments':comments ,'form': form}
    return render(request, 'book/details.html' , context)
  