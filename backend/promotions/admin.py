from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Promotion, Inscription

admin.site.register(Promotion)
admin.site.register(Inscription)