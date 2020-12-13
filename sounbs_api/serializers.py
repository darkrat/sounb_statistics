from rest_framework import serializers

class ListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
