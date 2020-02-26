from django.contrib import admin
from evaluation.models import D1A, D2

# Register your models here.
@admin.register(D1A)
class D1AAdmin(admin.ModelAdmin):
    pass


@admin.register(D2)
class D2Admin(admin.ModelAdmin):
    pass