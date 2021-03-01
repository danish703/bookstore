from django.urls import path
from .views import add,orderlist
urlpatterns=[
    path('add/',add,name='staffadd'),
    path('orderlist/',orderlist,name='orderlist'),
]