from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Company)
class Company_admin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Employee)
class Employee_admin(admin.ModelAdmin):
    list_display=['user','role']

@admin.register(Sections)  
class Sections_admin(admin.ModelAdmin):
    list_display=['component_name', 'position']

@admin.register(Website)
class Website_admin(admin.ModelAdmin):
    list_display=['website_name']

@admin.register(Images)
class Images_admin(admin.ModelAdmin):
    list_display=['img_type', 'item']

@admin.register(Configuration)
class Config_admin(admin.ModelAdmin):
    list_display=['config']


admin.site.register(Settings)
admin.site.register(Domain)
