from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ListPoem)
class ListPoemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'likes', 'dislikes')
    search_fields = ('title', 'content', 'author')