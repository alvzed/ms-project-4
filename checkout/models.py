from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_ID = models.CharField(max_length=254)
    is_delinquent = models.BooleanField()

    def __str__(self):
        return self.stripe_ID
