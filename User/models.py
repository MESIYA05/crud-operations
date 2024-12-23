from django.db import models

# Create your models here.

class Usersinfo(models.Model):
    Fullname = models.CharField(max_length=30)
    Email = models.EmailField()
    Dob = models.CharField(max_length=10)
    Password = models.CharField(max_length=15)
    Status = models.CharField(max_length=20)
    


    
    def __str__(self):
        return self.Fullname