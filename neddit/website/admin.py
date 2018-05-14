from django.contrib import admin
from django.contrib.auth.models import User
from .models import Comment, Post, Subneddit

# Register your models here.
admin.site.register(Subneddit)
admin.site.register(Post)
admin.site.register(Comment)
