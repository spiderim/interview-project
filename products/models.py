from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
import datetime

class Product(models.Model):
    compname=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)
    institute=models.CharField(max_length=100)

    def __str__(self):
        return str(self.hunter.username)

    def summary(self):
        return self.body[:300]

    @property
    def num_likes(self):
        return self.liked.all().count()

    def pub_date_preety(self):
        return self.pub_date.strftime('%b %e %Y')

LIKE_CHOICES=(
    ('Like','Like'),('Unlike','Unlike'), 

    )

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    value=models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

    def __str__(self):
        return str(self.product)


class Comment(models.Model):
    message=models.TextField()
    date_comment=models.DateTimeField()
    user_id=models.TextField()
    post_id=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id

    def date_preety(self):
        return self.date_comment.strftime('%b %e %Y')
    
        



