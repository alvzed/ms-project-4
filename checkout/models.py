from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.CharField(max_length=254)
    stripe_ID = models.CharField(max_length=254)
    is_delinquent = models.BooleanField()

    def __str__(self):
        return self.user
