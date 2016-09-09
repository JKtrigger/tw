from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#some 
class Message(models.Model):
    body  =   models.CharField        (max_length=140,blank=False,verbose_name='body')
    owner =   models.ForeignKey       (User,verbose_name='UIN')
    def __unicode__(self):
        return 'From :' + self.owner.username

