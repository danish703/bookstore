from django.urls import path
from .views import signin,signup,dashboard,signout
urlpatterns= [
  path('signup/',signup,name='signup'),
  path('signin/',signin,name='signin'),
  path('dashboard/',dashboard,name='dashboard'),
  path('signout/',signout,name='signout'),
]