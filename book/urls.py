from django.urls import path
from .views import add,booklist,edit
urlpatterns = [
  path('add/',add,name='bookadd'),
  path('edit/',edit,name='bookedit'),
  path('list/',booklist,name='booklist'),
]