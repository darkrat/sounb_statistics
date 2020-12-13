from django.urls import path
from sounbs_operator import views

urlpatterns = [
    path('', views.main, name='main'),
]