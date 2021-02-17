from django.db import models
from validators.validation import nameValidation,contactNoValidator
from django.contrib.auth.models import User
# Create your models here.
class Staff(models.Model):
    firstname = models.CharField(max_length=20,validators=[nameValidation,])
    lastname = models.CharField(max_length=20)
    contactNo = models.CharField(max_length=15,validators=[contactNoValidator,])
    address = models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname