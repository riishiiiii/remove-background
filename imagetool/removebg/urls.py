from django.urls import path
from . import views

urlpatterns = [
    path('remove-bg/', views.remove_bg, name='remove-bg'),
]