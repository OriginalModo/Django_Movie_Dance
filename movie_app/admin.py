from django.contrib import admin
from .models import *

@admin.register(Movie)
class ModelNameAdmin(admin.ModelAdmin):
    pass

