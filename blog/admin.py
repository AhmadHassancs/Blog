from django.contrib import admin

from .models import Post, Comment

# Register the models here that we have coded

admin.site.register(Post)
admin.site.register(Comment)