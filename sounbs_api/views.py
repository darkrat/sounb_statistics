from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ListSerializer, EventSerializer #, EventTitleSerializer
from .permission import HasCsrfTokenValid
from .models import Department,Event,EventForm,EventType,Theme
from django.middleware.csrf import _compare_salted_tokens, rotate_token
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
