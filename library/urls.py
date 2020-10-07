from django.urls import path
from . import views


urlpatterns = [
    path('', views.library, name='library'),
    path('<video_id>', views.player, name='player'),
    path('<video_id>/d/<review_id>',
         views.delete_review, name='delete_review'),
]
