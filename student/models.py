from django.db import models
from django.contrib.auth.models import User
from validators.validation import nameValidation,contactNoValidator
course  = (('CSIT','BSc.CSIT'),("bca","BCA"),("bit","BIT"))
# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=20,validators=[nameValidation,])
    lastname = models.CharField(max_length=20)
    contactNo = models.CharField(max_length=15,validators=[contactNoValidator,])
    course = models.CharField(max_length=15,choices=course)
    address = models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname

