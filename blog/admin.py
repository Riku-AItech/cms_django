# blog/admin.py

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')  # ←ここ！ created_at → created に修正

admin.site.register(Post, PostAdmin)

