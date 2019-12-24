from django.contrib import admin
from .models import ProjectUser

@admin.register(ProjectUser)
class ProjectUserAdmin(admin.ModelAdmin):
    pass
