from django.contrib import admin
from .models import Post ,Comment,CustomUser,Category
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)