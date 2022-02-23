from datetime import datetime, timezone, timedelta

# from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# from accountapp.models import User
from accountapp.models import CustomUser
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='article',
                               null=True)  # on_delete는 사용자가 없어지더라도 그대로 게시물은 남아있게하기위함
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.updated_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.updated_at.date()
            return str(time.days) + '일 전'
        else:
            return False
