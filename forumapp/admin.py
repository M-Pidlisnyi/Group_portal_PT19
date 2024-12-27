from django.contrib import admin
from .models import Topic, Thread, Post
# Register your models here.
admin.site.register(Topic)
admin.site.register(Thread)
admin.site.register(Post)