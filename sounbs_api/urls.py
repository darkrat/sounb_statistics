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
router.register(r'operator/events', EventOperatorView) 
router.register(r'operator/departments', DepartmentOperatorView)
router.register(r'operator/themes', ThemeOperatorView)
router.register(r'operator/eventtypes', EventTypeOperatorView)
router.register(r'operator/eventforms', EventFormOperatorView)
#router.register(r'administrator/eventforms', EventFormOperatorView) ???
urlpatterns = router.urls