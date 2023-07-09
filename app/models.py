from django.db import models

# Create your models here.


class Register(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    Phone1 = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=15)
    year = models.CharField(max_length=10)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.fname+" "+self.lname
