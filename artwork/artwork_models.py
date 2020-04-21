from django.db import models
import os
from uuid import uuid4
from .utils import *
from django.conf import settings
from PIL.Image import LANCZOS, open
from _io import BytesIO
from django.core.files.base import ContentFile
from django.template.defaultfilters import default
import pandas as pd


class School(models.Model):
    natemis = models.IntegerField(blank=True, null=True, default=0)
    province = models.CharField(blank=True, null=True, max_length=100, choices=Province.provincelist())
    name = models.CharField(max_length=200, db_index=True)
    region = models.CharField(blank=True, null=True, max_length=200, default="")

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
        null=False, blank=False, on_delete=models.CASCADE)
    learnergrade = models.CharField(blank=True, null=True, max_length=100)
    school = models.ForeignKey(School, blank=True, null=True, on_delete=models.SET_NULL)
    teachername = models.CharField(blank=True, max_length=300)
    teacherphone = models.CharField(blank=True, null=True, max_length=100)
    teacheremail = models.CharField(blank=True, null=True, max_length=200)
    worktitle = models.CharField(blank=True, null=True, max_length=300)
    workfile = models.FileField(blank=True, null=True, upload_to='works')
    thumbnail = models.FileField(blank=True, null=True, upload_to='works')
    workfileCropped = models.TextField(blank=True, default="", null=True)
    comment = models.TextField(blank=True, default="", null=True)
    workformulafile = models.FileField(null=True, blank='True', upload_to='formulas')
    workapproved = models.BooleanField(default=False)
    bioapproved = models.BooleanField(default=False)
    qapproved = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    question1 = models.TextField(blank=True)
    question2 = models.TextField(blank=True)
    question3 = models.TextField(blank=True)
    submitted = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Status.statuslist(), default=-1)

    class Meta:
        ordering = ['submitted']

    def save(self, *args, **kwargs):
        self.make_thumbnail()
        print("save initiation >>> ", self)
        if self.status == 0:
            fname = self.owner.first_name
            lname = self.owner.last_name
            subject = "MathArt Portal - Registration Successful"
            message = "Dear {0} {1}, you have successfully registered in mathartcompetition.\n\nPlease go on and finish your artwork submission".format(fname, lname)
            mailmsg1 = (subject, message, 'mathart.co.za@gmail.com', [self.owner.username])
        super(Artwork, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return "work_details/{self.id}"

    def __str__(self):
        return ''

    def get_artwork_status(self):
        return Status(self.status).name

    def make_thumbnail(self):
        if self.workfile.name is None or len(self.workfile.name) <= 0:
            return False
        if self.thumbnail.name != None and self.workfile.name.split(".")[0] in self.thumbnail.name :
            return False
        image = open(self.workfile, 'r')
        ratio = image.width / 200
        THUMB_SIZE = (200, image.height / ratio)
        image.thumbnail(THUMB_SIZE, LANCZOS)
        thumb_name, thumb_extension = os.path.splitext(self.workfile.name)
        thumb_extension = thumb_extension.lower()
        thumb_filename = thumb_name + '_thumb' + thumb_extension
        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension in ['.png']:
            FTYPE = 'PNG'
        else:
            return False 
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
        return True


def get_model_field_names(model, ignore_fields=['content_object']):
#     model_fields = model.owner._meta.get_fields()
#     author_field_names = list(set([f.name for f in model_fields if f.name not in ignore_fields]))    
    model_fields = model._meta.get_fields()
    model_field_names = list(set([f.name for f in model_fields if f.name not in ignore_fields]))
#     author_field_names.append(model_field_names)
    return model_field_names


def get_lookup_fields(model, fields=None):
    model_field_names = get_model_field_names(model)
    if fields is not None:
        lookup_fields = []
        for x in fields:
            if "__" in x:
                lookup_fields.append(x)
            elif x in model_field_names:
                lookup_fields.append(x)
    else:
        lookup_fields = model_field_names
    return lookup_fields


def qs_to_dataset(qs, fields=None):
    lookup_fields = get_lookup_fields(qs.model, fields=fields)
    return list(qs.values(*lookup_fields))


def convert_to_df(qs, fields=None, index=None):
    lookup_fields = get_lookup_fields(qs.model, fields=fields)
    index_col = None
    if index in lookup_fields:
        index_col = index
    elif "id" in lookup_fields:
        index_col = 'id'
    values = qs_to_dataset(qs, fields=fields)
    df = pd.DataFrame.from_records(values, columns=lookup_fields, index=index_col)
    return df
