from django.contrib import admin
from .models import School, Artwork

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']
    #prepopulated_fields = {''}

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['surname', 'firstname', 'worktitle',
                     'school', 'dob',
                      'parentname', 'teachername']
    list_filter = ['surname', 'school', 'worktitle']
    #list_editable = ['']
