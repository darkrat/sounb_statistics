from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ListSerializer, EventSerializer, DictionarySerializer #, EventTitleSerializer
from .permission import HasCsrfTokenValid
from .models import Department,Event,EventForm,EventType,Theme
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

# Operator Views
class DepartmentOperatorView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [HasCsrfTokenValid,]
    
    def list(self, request):
        result = ""
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = DictionarySerializer(queryset, many=True)
        for dep in serializer.data:
            result += "'%s':'%s'," % (dep.id, dep.title) 
        return Response({"data": "{%s}" % result})

class EventOperatorView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [HasCsrfTokenValid,]
    def get(self, request):
        serializer = EventSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = EventSerializer(queryset, many=True)
        return Response({"data": serializer.data})
