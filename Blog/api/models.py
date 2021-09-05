from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.
class CustomUser(AbstractUser):
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()

class Staff(CustomUser):
    class Meta:
        proxy = True

class Visitor(CustomUser):
    class Meta:
        proxy = True

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('CustomUser', related_name='posts', on_delete=models.CASCADE)
    class Meta:
        ordering = ('created',)


class Comment(models.Model):
    class Meta:
        ordering = ('created',)

    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('CustomUser', related_name='comments', on_delete=models.CASCADE)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=100,blank=False)
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,related_name='categories')
    posts = models.ManyToManyField(Post,related_name='categories',blank=True)