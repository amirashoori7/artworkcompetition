from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import *
from django.urls import reverse

class School(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    address = models.CharField(max_length=500)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    worktitle = models.CharField(max_length=300)
    school = models.ForeignKey(School,
                               related_name='artworks',
                               on_delete=models.CASCADE)
    surname = models.CharField(max_length=200, db_index=True)
    firstname = models.CharField(max_length=200)
    workfile = models.ImageField(upload_to='works')
    email = models.EmailField(max_length=100)
    dob = models.DateField(null=True)
    age = models.IntegerField(editable=False, null=True)
    parentname = models.CharField(blank=True, max_length=200)
    parentphone = models.CharField(blank=True, null=True, max_length=100)
    parentemail = models.EmailField(blank=True, max_length=100)
    learnergrade = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
    teachername = models.CharField(blank=True, max_length=300)
    teacherphone = models.CharField(blank=True, null=True, max_length=100)
    teacheremail = models.EmailField(blank=True, max_length=100)
    testimonial = models.BooleanField(default=False)
    question1 = models.TextField(blank=True)
    question2 = models.TextField(blank=True)
    question3 = models.TextField(blank=True)
    submitted = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()
    d1a = models.OneToOneField('evaluation.D1A', blank=True,
                                    null=True, on_delete=models.CASCADE)
    d1b = models.ForeignKey('evaluation.D1B', blank=True,
                                 null=True, on_delete=models.CASCADE)
    d2 = models.ForeignKey('evaluation.D2', blank=True,
                                 null=True, on_delete=models.CASCADE)
    d3 = models.ForeignKey('evaluation.D3', blank=True,
                                 null=True, on_delete=models.CASCADE)

    class Meta:
        #unique_together = ['surname', 'email']
        ordering = ['surname']
        index_together = ['id', 'surname']

    def save(self, *args, **kwargs):
        today = date.today()
        delta = relativedelta(today, self.dob)
        self.age = delta.years
        self.status = 1
        super(Artwork, self).save(*args, **kwargs)

    #define the returened url when the submit button hit
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
