from rest_framework import serializers
from .models import Event
class ListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'ExpositionTitle', 'HasPoster', 'HasPhotos', 'StartDate', 'EndDate', 'Title', 'Description', 'Author', 'Location', 'VisitorCount', 'ChildVisitorCount', 'JuniorVisitorCount', 'BooksOnDisplayCount', 'IssuedBooksCount', 'Department_id', 'EventForm_id', 'EventType_id', 'Owner_id')