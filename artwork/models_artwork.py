from django.db import models
import os
from uuid import uuid4
from .utils import Status
from django.conf import settings
from PIL.Image import LANCZOS, open
from _io import BytesIO
from django.core.files.base import ContentFile


class School(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    region = models.CharField(blank=True, null=True, max_length=200)
    province = models.CharField(blank=True, null=True, max_length=200)
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
    teacheremail = models.CharField(blank=True, null=True, max_length=100)
    worktitle = models.CharField(blank=True, null=True, max_length=300)
    workfile = models.FileField(blank=True, null=True, upload_to='works')
    thumbnail = models.FileField(blank=True, null=True, upload_to='works')
    workfileCropped = models.TextField(blank=True, default="", null=True)
    comment = models.TextField(blank=True, default="", null=True)
    workformulafile = models.FileField(null=True, blank='True',upload_to='formulas')
    workapproved = models.BooleanField(default=False)
    bioapproved = models.BooleanField(default=False)
    qapproved = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    question1 = models.TextField(blank=True, max_length=100)
    question2 = models.TextField(blank=True)
    question3 = models.TextField(blank=True)
    submitted = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Status.statuslist(), default=-1)

    class Meta:
        ordering = ['submitted']

    def save(self, *args, **kwargs):
        self.make_thumbnail()
        print("save initiation >>> ", self)
#         if(self.id == 0):
#             handleFile()
        super(Artwork, self).save(*args, **kwargs)

    # define the returened url when the submit button hit
    def get_absolute_url(self):
        return "work_details/{self.id}"

    def __str__(self):
        return '' 

    def get_artwork_status(self):
        return Status(self.status).name

    def make_thumbnail(self):
        if self.workfile.name is None or len(self.workfile.name) <=0:
            return False
        image = open(self.workfile)
        ratio = image.width / 200
        THUMB_SIZE = (200, image.height/ratio)
        image.thumbnail(THUMB_SIZE, LANCZOS)

        thumb_name, thumb_extension = os.path.splitext(self.workfile.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        else:
            return False    # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True
'''
#Custom Object Manager
class CustomManager(models.Model):
    def get_queryset(self):
        return super(CustomManager,
                     self).get_queryset()
                          .filter(status='approved')
'''
