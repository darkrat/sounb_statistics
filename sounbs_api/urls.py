from rest_framework.routers import DefaultRouter
from .views import *
app_name = "sounbs_api"
# app_name will help us do a reverse look-up latter.
router = DefaultRouter()
router.register(r'departments', DepartmentView, basename='user')
router.register(r'themes', ThemeView, basename='user')
router.register(r'eventtypes', EventTypeView, basename='user')
router.register(r'eventforms', EventFormView, basename='user')
router.register(r'events', EventView, basename='user')
urlpatterns = router.urls