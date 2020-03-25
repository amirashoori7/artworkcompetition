from django.contrib import admin
from evaluation.models import D1A, D2, D1B

# Register your models here.
@admin.register(D1A)
class D1AAdmin(admin.ModelAdmin):
    pass

@admin.register(D1B)
class D1BAdmin(admin.ModelAdmin):
    pass

@admin.register(D2)
class D2Admin(admin.ModelAdmin):
    pass

# @admin.register(D3)
# class D3Admin(admin.ModelAdmin):
#     pass