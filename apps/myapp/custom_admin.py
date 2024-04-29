# admin.py
from django.contrib import admin
from .models import AndroidApp, Task, TaskCompletion

class CustomAdminSite(admin.AdminSite):
    site_header = 'Custom Admin Interface'  # Customize the header text
    site_title = 'Custom Admin'  # Customize the browser tab title

custom_admin_site = CustomAdminSite(name='custom_admin')  # Create a custom admin site

# Register your models with the custom admin site
custom_admin_site.register(AndroidApp)
custom_admin_site.register(Task)
custom_admin_site.register(TaskCompletion)
