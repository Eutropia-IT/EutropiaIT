from django.contrib import admin

# model
from .models import Client, Technology, Project, Employee,Blog, Review

# Register your models here.
admin.site.register(Client)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(Employee)
admin.site.register(Blog)
admin.site.register(Review)
