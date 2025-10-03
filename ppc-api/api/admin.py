from django.contrib import admin
from .models import User, Profile, Client, Project

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Project)