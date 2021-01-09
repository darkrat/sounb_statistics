from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Event, Department

class ListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'Theme', 'ExpositionTitle', 'HasPoster', 'HasPhotos', 'StartDate', 'EndDate', 'Title', 'Description', 'Author', 'Location', 'VisitorCount', 'ChildVisitorCount', 'JuniorVisitorCount', 'BooksOnDisplayCount', 'IssuedBooksCount', 'Department_id', 'EventForm_id', 'EventType_id', 'Owner_id')

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
