from django.db import models

class UserStatus(models.Model):
    userName = models.TextField()
    atCafe = models.BooleanField()
    description = models.TextField()
    teach = models.BooleanField()

#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
# 
# class Choice(models.Model):
#     poll = models.ForeignKey(Poll)
#     choice = models.CharField(max_length=200)
#     votes = models.IntegerField()
