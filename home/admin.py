from django.contrib import admin
from .models import Distillery, Whiskey

# Register your models here.

admin.site.register(Distillery)
admin.site.register(Whiskey)
