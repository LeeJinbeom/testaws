from django.contrib import admin
from .models import Todo, TodoGroup

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass

@admin.register(TodoGroup)
class TodoGroupAdmin(admin.ModelAdmin):
    pass
