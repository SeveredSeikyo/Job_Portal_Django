from django.contrib import admin
from .models import Job

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display=['company','role','qualification','salary','published_on']

admin.site.register(Job,JobAdmin)