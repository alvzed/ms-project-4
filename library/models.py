from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    slug = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.slug

    def get_friedly_name(self):
        return self.name


class Video(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    description = models.TextField()
    video_link = models.CharField(max_length=254)
    pg = models.DecimalField(max_digits=2, decimal_places=0, null=True,
                             blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField()
    thumbsup = models.PositiveIntegerField(default=0)
    thumbsdown = models.PositiveIntegerField(default=0)

    def __str__(self):
        return super().__str__()
