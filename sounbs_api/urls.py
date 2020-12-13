from django.urls import path
from .views import DepartmentView
app_name = "sounbs_api"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('departments/', DepartmentView.as_view()),
]