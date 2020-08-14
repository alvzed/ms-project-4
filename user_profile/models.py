from django.db import models
from django.contrib.auth.models import User
from library.models import Video


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, null=True, blank=True)
    history = models.ForeignKey(Video, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return ''
