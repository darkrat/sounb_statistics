from django.urls import path
from .views import *
app_name = "sounbs_api"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('departments/', DepartmentView.as_view()),
    path('themes/', ThemeView.as_view()),
    path('evettypes/', EventTypeView.as_view()),
    path('eventforms/', EventFormView.as_view()),
    path('events/', EventView.as_view()),
]