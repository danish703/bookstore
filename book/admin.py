from django.contrib import admin
from .models import Book,BookOrder
# Register your models here.
admin.site.register([Book,BookOrder])