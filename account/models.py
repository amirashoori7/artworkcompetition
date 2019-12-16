from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import *
from django.urls import reverse

ROLES = (
    ('1', 'Judge 1'),
    ('2', 'Judge 2'),
    ('3', 'Judge 3'),
)

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=1, choices=ROLES)

    def __str__(self):
        return self.name
