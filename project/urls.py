from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('detail/', views.detail, name='detail'),
]