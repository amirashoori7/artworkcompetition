from django.contrib import admin
from .models_account import ProjectUser

@admin.register(ProjectUser)
class ProjectUserAdmin(admin.ModelAdmin):
    pass
