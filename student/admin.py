from django.contrib import admin
from .models import Teachers , Students
# Register your models here.


@admin.register(Teachers)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Students)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
