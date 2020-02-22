from django.contrib import admin
from artwork.artwork_models import School, Artwork

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name']
    #prepopulated_fields = {''}

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['worktitle', 'school']
    list_filter = ['school', 'worktitle']
    #list_editable = ['']
