from django.db import models

# Create your models here.
class LabelsAndInstructions(models.Model):
    '''
    
    '''
    key = models.CharField(max_length = 256, unique = True, name = 'key', db_column = 'key')
    description = models.TextField(name = 'description', db_column = 'description')
    created = models.DateTimeField(auto_now_add = True, name = 'created', db_column = 'created')
    changed = models.DateTimeField(auto_now = True, name = 'changed', db_column = 'changed')

class Languages(models.Model):
    '''
    
    '''
    language_code = models.CharField(max_length = 7, name = 'language_code', db_column = 'language_code')
    name = models.CharField(max_length = 256, name = 'name', db_column = 'name')

class LabelsAndInstructionsLanguages(models.Model):
    '''
    
    '''
    label_or_instruction = models.ForeignKey(LabelsAndInstructions, name = 'label_or_instruction', db_column = 'label_or_instruction', on_delete = models.CASCADE)
    language = models.ForeignKey(Languages, name = 'language', db_column = 'language', on_delete = models.CASCADE)
    value = models.TextField(name = 'value', db_column = 'value')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = [
                    'label_or_instruction',
                    'language',
                ],
                name = 'unique appversion'
            )
        ]

class RequestsTypes(models.Model):
    '''
    
    '''
    name = models.CharField(max_length = 256, name = 'name', db_column = 'name')
    created = models.DateTimeField(auto_now_add = True, name = 'created', db_column = 'created')
    changed = models.DateTimeField(auto_now = True, name = 'changed', db_column = 'changed')

class RequestsLog(models.Model):
    '''
    
    '''
    created = models.DateTimeField(auto_now_add = True, name = 'created', db_column = 'created')
    type = models.ForeignKey(RequestsTypes, name = 'type', db_column = 'type', on_delete = models.CASCADE)
    title = models.CharField(max_length = 256, name = 'title', db_column = 'title')
    description = models.TextField(name = 'description', db_column = 'description')
