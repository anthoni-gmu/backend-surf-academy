from django.db import models
from datetime import datetime



class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    status = models.BooleanField(default=True)
    join = models.DateField(default=datetime.now)
    phone = models.IntegerField()
    dni=models.CharField(max_length=255,unique=True)
    
    
    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name
