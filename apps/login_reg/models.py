from __future__ import unicode_literals

from django.db import models

import bcrypt
import re

class UserManager(models.Manager):
    def loginVal(self, postdata):
        result={'status':True, 'errors':[],'user':None}
        users=self.filter(user_name=postdata['user_name']) 
        if len(users)<1:
            result['status']=False
        else:
            if bcrypt.checkpw(postdata['password'].encode(), users[0].password.encode()):
                result['user']=users[0]
            else: 
                result['status']=False
            return result

        
    def creator(self,postdata):
        user = self.create(first_name= postdata['first_name'], user_name=postdata['user_name'], password=bcrypt.hashpw(postdata['password'].encode(), bcrypt.gensalt()))
        return user
    def validate(self, postdata):
        result={'status':True, 'errors':[]}
        if len(postdata['first_name'])<3:
            result['errors'].append('Your first name is too short')
            result['status']=False
        if len(postdata['user_name'])<3:
            result['errors'].append('Your user name is too short')
            result['status']=False
        # if not re.match("[^@]+@[^@]+\.[^@]+", postdata['email']):
        #     result['errors'].append('Email is not valid')
        #     result['status']=False
        if (postdata['password']!=postdata['c_password']):
            result['errors'].append('Passwords do not match')
            result['status']=False
        if len(postdata['password'])<5:
            result['errors'].append('Password needs to be 5 characters long at least')
            result['status']=False
        if len(self.filter(user_name = postdata['user_name']))>0:
            result['errors'].append('User with this user_name already exists')
            result['status']=False
        return  result





class User(models.Model):
    first_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hired_date=models.DateField(null=True, blank=True)
    objects =UserManager()



