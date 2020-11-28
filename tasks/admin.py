from django.contrib import admin
from .models import Task


class TasksAdmin(admin.ModelAdmin):
    """
    Register User Profiles to admin profiles
    """
    list_display = ('header', 'text', 'published', 'avatar', 'exp', 'status')


# admin.site.register(Task, TasksAdmin)
