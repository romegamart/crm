from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register((Employee,Client,Client_History))