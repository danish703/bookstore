from django.urls import path
from .views import add,dashboard
urlpatterns=[
    path('add/',add,name='studentadd'),
    path('dashboard/',dashboard,name='studentdashboard')
]