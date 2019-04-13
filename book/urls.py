

from django.urls import path, include 
from . import views


urlpatterns = [
    path('', views.index ),
    path('book_details/<int:id>', views.book_details)
]
