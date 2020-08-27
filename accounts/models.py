from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    institute=models.CharField(max_length=100)
    phone_num=models.CharField(max_length=15,default='0000000000')
    age=models.IntegerField(default=0)

    def __str__(self):
        return  str(self.user.username)


