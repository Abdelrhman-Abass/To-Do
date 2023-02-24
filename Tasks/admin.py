from django.contrib import admin

from  .models import *
# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ['slug' ,'task_name','user']
    list_filter = ['task_name','user']

class UserAdmin(admin.ModelAdmin):
    list_display = ['user' ,'name']
    list_filter = ['user' ,'name']

admin.site.register(Task , TasksAdmin)
admin.site.register(UserProfile ,UserAdmin)
# admin.site.register(Tokens)