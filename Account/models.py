from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER=(('M','Male'),('F','Female'))
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    fullname=models.CharField(max_length=20)
    gender = models.CharField(max_length=150, choices=GENDER)
    phone=models.CharField(max_length=11)


    def __str__(self):
        return self.fullname