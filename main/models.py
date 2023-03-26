from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Discount(models.Model):
    txn_hash = models.TextField(default="none")
    name = models.TextField(default="none")
    wallet = models.TextField(default="none")
    age = models.TextField(default="none")
    
    status = models.BooleanField(default=False)
    
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name




class Domain(models.Model):
    token_id = models.TextField(default="none")
    name = models.TextField(default="none")
    age = models.TextField(default="none")
    address = models.TextField(default="none")
    first_address = models.TextField(default="none")
    description = models.TextField(default="none")
    image = models.TextField(default="none")
    
    status = models.BooleanField(default=True)
    
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.address