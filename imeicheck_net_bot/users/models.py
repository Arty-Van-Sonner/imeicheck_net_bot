from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    '''
    
    '''
    user_id = models.IntegerField(unique = True, name = 'user_id', db_column = 'user_id', null = True)
    access_opened = models.BooleanField(default = True, name = 'access_opened', db_column = 'access_opened')
    created = models.DateTimeField(auto_now_add = True, name = 'created', db_column = 'created')
    changed = models.DateTimeField(auto_now = True, name = 'changed', db_column = 'changed')