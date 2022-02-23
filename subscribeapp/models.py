# from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# from accountapp.models import User
from accountapp.models import CustomUser
from projectapp.models import Project

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        unique_together = ('user', 'project') #user와 project를 합쳐 유니크하게 해서 프로젝트당 하나만 구독을 누를수있게 만들기위함
