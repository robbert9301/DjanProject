# from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from accountapp.models import CustomUser
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment') #Article table에 연결
    writer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.TextField(null=False)

    created_at = models.DateField(auto_now_add=True, null=True)