from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ListSerializer

from .models import Department,Event,EventForm,EventType,Theme
# Create your views here.

# Department
class DepartmentView(APIView):
    def get(self, request):
        objects = Department.objects.all()
        serializer = ListSerializer(objects, many=True)
        return Response({"departments": serializer.data})
#EventType
class EventTypeView(APIView):
    def get(self, request):
        objects = EventType.objects.all()
        serializer = ListSerializer(objects, many=True)
        return Response({"eventtypes": serializer.data})
#EventForm
class EventFormView(APIView):
    def get(self, request):
        objects = EventForm.objects.all()
        serializer = ListSerializer(objects, many=True)
        return Response({"eventforms": serializer.data})
#Theme
class ThemeView(APIView):
    def get(self, request):
        objects = Theme.objects.all()
        serializer = ListSerializer(objects, many=True)
        return Response({"themes": serializer.data})
#Event
class EventView(APIView):
    def get(self, request):
        objects = Event.objects.all()
        serializer = ListSerializer(objects, many=True)
        return Response({"events": serializer.data})