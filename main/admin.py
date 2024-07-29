from django.contrib import admin
from .models import Category, Tag, Video, Comment, CustomUser
# Register your models here.


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(CustomUser)

