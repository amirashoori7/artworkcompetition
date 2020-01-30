from django.db import models
from django.template.defaultfilters import default
import os
from uuid import uuid4
from .utils import Status
from account.models_account import ProjectUser
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.conf import settings


class School(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    region = models.CharField(blank=False, null=True, max_length=200)
    province = models.CharField(blank=False, null=True, max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print("save initiation >>> ", self)
        super(School, self).save(*args, **kwargs)

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

class Artwork(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.CASCADE)
    learnergrade = models.CharField(blank=True, null=True, max_length=100)
    school = models.CharField(blank=False, null=False, max_length=100)
    teachername = models.CharField(blank=True, max_length=300)
    teacherphone = models.CharField(blank=False, null=True, max_length=100)
    teacheremail = models.CharField(blank=False, null=True, max_length=100)
    worktitle = models.CharField(blank=False, null=True, max_length=300)
    workfile = models.FileField(upload_to='works')
    workfileCropped = models.TextField(blank=False, default="", null=False)
    workformulafile = models.FileField(null=True, blank='True',upload_to='formulas')
    workapproved = models.BooleanField(default=False)
    bioapproved = models.BooleanField(default=False)
    qapproved = models.BooleanField(default=False)
    question1 = models.TextField(blank=False)
    question2 = models.TextField(blank=False)
    question3 = models.TextField(blank=False)
    submitted = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Status.statuslist(), default=-1)

    class Meta:
        ordering = ['submitted']

    def save(self, *args, **kwargs):
        print("save initiation >>> ", self)
#         if(self.id == 0):
#             handleFile()
        super(Artwork, self).save(*args, **kwargs)

    # define the returened url when the submit button hit
    def get_absolute_url(self):
        return "work_details/{self.id}"

    def __str__(self):
        return '%s %s' % (self.dob, self.parentname)

    def get_artwork_status(self):
        return Status(self.status).name


'''
#Custom Object Manager
class CustomManager(models.Model):
    def get_queryset(self):
        return super(CustomManager,
                     self).get_queryset()
                          .filter(status='approved')
'''
