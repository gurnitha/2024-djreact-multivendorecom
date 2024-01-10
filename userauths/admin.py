# userauths/models.py

# Django and third parties modules
from django.contrib import admin

# Locals
from userauths.models import User, Profile 

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)