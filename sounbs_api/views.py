from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DepartmentSerializer

from .models import Department
# Create your views here.

class DepartmentView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response({"departments": serializer.data})