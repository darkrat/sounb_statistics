from rest_framework.routers import DefaultRouter
from .views import *
app_name = "sounbs_api"
# app_name will help us do a reverse look-up latter.
router = DefaultRouter()
router.register(r'departments', DepartmentView)
router.register(r'themes', ThemeView)
router.register(r'eventtypes', EventTypeView)
router.register(r'eventforms', EventFormView)
router.register(r'events', EventView)
router.register(r'metaevent', EventTitleView)
urlpatterns = router.urls