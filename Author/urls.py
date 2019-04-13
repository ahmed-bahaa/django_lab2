
from django.urls import path, include 
from . import views


urlpatterns = [
    path('<int:value>', views.show , name="author_details" )
]
