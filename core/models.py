from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import EmailField
from django.db.models.fields import DateTimeField






class User(models.Model):
    firstName = CharField(max_length=30)
    lastName = CharField(max_length=30)
    email = EmailField(max_length=50, unique=True)
    password = CharField(max_length=30)
    rol = CharField(max_length=20, default='USER')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


    
