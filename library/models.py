from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friedly_name(self):
        return self.friendly_name


class Video(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    description = models.TextField()
    video_link = models.CharField(max_length=254)
    pg = models.DecimalField(max_digits=2, decimal_places=0, null=True,
                             blank=True)

    def __str__(self):
        return self.title
