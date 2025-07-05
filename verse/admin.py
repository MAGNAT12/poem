from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ListPoem)
class ListPoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content', 'author')