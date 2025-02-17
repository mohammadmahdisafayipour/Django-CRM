from django.contrib import admin
from .models import Record
# Register your models here.



class RecordAdmin(admin.ModelAdmin):
    list_display = ['__all__']
    
admin.site.register(Record)