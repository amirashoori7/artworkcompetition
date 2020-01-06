from django.db import models
from django.template.defaultfilters import default
import os
from uuid import uuid4


class School(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    address = models.CharField(max_length=500)
    province = models.IntegerField(default=0,blank=False,null=False)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

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
    firstname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(blank=True, null=True, max_length=100)
    dob = models.DateField(blank=True, null=True)
    cellphone = models.CharField(blank=True, null=True, max_length=100)
    learnergrade = models.CharField(blank=True, null=True, max_length=100)
    bioapproved = models.BooleanField(default=False)
    parentname = models.CharField(blank=True, max_length=200)
    parentphone = models.CharField(blank=True, null=True, max_length=100)
    parentemail = models.CharField(blank=False, null=False, max_length=100)
    school = models.CharField(blank=False, null=False, max_length=100)
    teachername = models.CharField(blank=True, max_length=300)
    teacherphone = models.CharField(blank=False, null=True, max_length=100)
    teacheremail = models.CharField(blank=False, null=True, max_length=100)
    worktitle = models.CharField(blank=False, null=True, max_length=300)
    workfile = models.FileField(upload_to='works')
    workfileCropped = models.TextField(blank=False, default="", null=False)
    workformulafile = models.FileField(null=True, blank='True',upload_to='formulas')
    workapproved = models.BooleanField(default=False)
    question1 = models.TextField(blank=False)
    question2 = models.TextField(blank=False)
    question3 = models.TextField(blank=False)
    qapproved = models.BooleanField(default=False)
    submitted = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    d1a = models.ForeignKey('evaluation.D1A', blank=True,
                                    null=True, on_delete=models.CASCADE)
    d1b = models.ForeignKey('evaluation.D1B', blank=True,
                                 null=True, on_delete=models.CASCADE)
    d2 = models.ForeignKey('evaluation.D2', blank=True,
                                 null=True, on_delete=models.CASCADE)
    d3 = models.ForeignKey('evaluation.D3', blank=True,
                                 null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def save(self, *args, **kwargs):
        print("save initiation >>> ", self)
#         if(self.id == 0):
#             handleFile()
        super(Artwork, self).save(*args, **kwargs)

    # define the returened url when the submit button hit
    def get_absolute_url(self):
        return "work_details/{self.id}"

    def __str__(self):
        return '%s %s' % (self.surname, self.firstname)

'''
#Custom Object Manager
class CustomManager(models.Model):
    def get_queryset(self):
        return super(CustomManager,
                     self).get_queryset()
                          .filter(status='approved')
'''
