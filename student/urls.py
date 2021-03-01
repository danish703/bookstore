from django.urls import path
from .views import add,dashboard,bookrequest
urlpatterns=[
    path('add/',add,name='studentadd'),
    path('dashboard/',dashboard,name='studentdashboard'),
    path('bookrequest/<int:id>',bookrequest,name='bookrequest')
]