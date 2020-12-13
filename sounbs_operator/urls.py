from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.main, name='main'),
]