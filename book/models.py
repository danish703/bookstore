from django.db import models
from student.models import Student
from staff.models import Staff
# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=40)
    isbn = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True,blank=True)
    coverimage = models.ImageField(upload_to='book/')

    def __str__(self):
        return self.name


class BookOrder(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    issueDate = models.DateTimeField(auto_now_add=True)
    returnDate = models.DateTimeField()
    issueBy = models.ForeignKey(Staff,on_delete=models.CASCADE)

    def __str__(self):
        return self.student.firstname