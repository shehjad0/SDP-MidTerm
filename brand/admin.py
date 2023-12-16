from django.contrib import admin
from .models import BrandModel
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=('name','slug')
    
admin.site.register(BrandModel, BrandAdmin)