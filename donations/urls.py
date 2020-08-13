from django.urls import path
from . import views


urlpatterns = [
    path('', views.donate, name='donate'),
    path('success/<str:args>', views.success, name='success')
]
