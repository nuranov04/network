from django.contrib import admin
from .models import Post, PostImage, Like

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Like)