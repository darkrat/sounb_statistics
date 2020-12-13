from rest_framework import serializers
class DepartmentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)