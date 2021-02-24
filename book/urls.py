from django.urls import path
from .views import add,booklist,edit,bookdetails,deleteBook
urlpatterns = [
  path('add/',add,name='bookadd'),
  path('edit/<int:id>',edit,name='bookedit'),
  path('list/',booklist,name='booklist'),
  path('details/<int:id>',bookdetails,name='details'),
  path('delete/<int:id>',deleteBook,name='delete')
]