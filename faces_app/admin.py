from django.contrib import admin

from faces_app.models import Message, Post, Profile, Comment


admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Message)
# Register your models here.
