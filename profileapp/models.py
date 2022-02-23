# from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from accountapp.models import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile') #on_delete cascade는 유저가 사라질때 위에있는 profile도 같이 사라지게 만들어줌

    # image = models.ImageField(upload_to='profile/', null=True) #media 밑에 profile에 업로드 됨
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
