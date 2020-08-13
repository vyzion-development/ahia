from django.contrib import admin
from .models import Profile, Category, Post, Chat, Comment, Asset
# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Chat)
admin.site.register(Comment)
admin.site.register(Asset)