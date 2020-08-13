from django.urls import path
from . import views


urlpatterns = [
    path('', views.library, name='library'),
    path('<video_id>', views.player, name='player'),
    path('g/<category>', views.category, name='category')
]
