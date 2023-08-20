from django.contrib import admin
from django.db import models


# Create your models here.

class Profile(models.Model):
    Name = models.CharField(max_length=50, null=True,blank=True )
    Email = models.EmailField(max_length=25)
    Age = models.ImageField(null=True,blank=True)
    Image = models.ImageField(upload_to='Prof_pic/', default='default.png')
    Address = models.TextField(max_length=50, null=True, blank=True)
    Phone_Number = models.TextField(max_length=15, null=True, blank=True)
    Date_Of_Birth = models.TextField(max_length=25,null=True, blank=True)
    Gender = models.CharField(max_length=8, null=True, blank=True)
    Religion = models.CharField(max_length=8,null=True, blank=True)

    def __str__(self):
        return str(self.Name)
