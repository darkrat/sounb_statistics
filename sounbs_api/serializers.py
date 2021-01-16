from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Event, Department, EventType, EventForm, Theme

class ListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','title')

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ('id','title')

class EventFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventForm
        fields = ('id','title')

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id','title')

class EventSerializer(serializers.ModelSerializer):
    Department_id = serializers.CharField(source='Department.id', read_only=True)
    Theme_id = serializers.CharField(source='Theme.id', read_only=True)
    EventForm_id = serializers.CharField(source='EventForm.id', read_only=True)
    EventType_id = serializers.CharField(source='EventType.id', read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'Theme_id', 'ExpositionTitle', 'HasPoster', 'HasPhotos', 'StartDate', 'EndDate', 'Title', 'Description', 'Author', 'Location', 'VisitorCount', 'ChildVisitorCount', 'JuniorVisitorCount', 'BooksOnDisplayCount', 'IssuedBooksCount', 'Department_id', 'EventForm_id', 'EventType_id', 'Owner_id')

# class EventTitleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(EventTitleSerializer, self).__init__(*args, **kwargs)

#         if 'labels' in self.fields:
#             raise RuntimeError(
#                 'You cant have labels field defined '
#                 'while using EventTitleSerializer'
#             )

#         self.fields['labels'] = SerializerMethodField()

#     def get_labels(self, *args):
#         labels = {}

#         for field in self.Meta.model._meta.get_fields():
#             if field.name in self.fields:
#                 labels['title'] = field.verbose_name
#         return labels
