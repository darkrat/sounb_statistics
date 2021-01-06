from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ListSerializer, EventSerializer

from .models import Department,Event,EventForm,EventType,Theme,EventTitleSerializer
# Create your views here.

# Department
class DepartmentView(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = Department.objects.all()
#EventType
class EventTypeView(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = EventType.objects.all()
#EventForm
class EventFormView(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = EventForm.objects.all()
#Theme
class ThemeView(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = Theme.objects.all()
#Event
class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventTitle(viewsets.ModelViewSet):
    serializer_class = EventTitleSerializer
    queryset = Event.objects.all()
    