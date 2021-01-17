from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Event, Department, EventType, EventForm, Theme

class ListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    depth = 1

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','title')
        depth = 1

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ('id','title')
        depth = 1

class EventFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventForm
        fields = ('id','title')
        depth = 1

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id','title')
#        depth = 1

class EventSerializer(serializers.ModelSerializer):
#    Department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all()) # serializers.CharField(source='Department.id', read_only=True)
#    Theme_id = serializers.PrimaryKeyRelatedField(queryset=Theme.objects.all()) # serializers.CharField(source='Theme.id', read_only=True)
#    EventForm_id = serializers.PrimaryKeyRelatedField(queryset=EventForm.objects.all()) # serializers.CharField(source='EventForm.id', read_only=True)
#    EventType_id = serializers.PrimaryKeyRelatedField(queryset=EventType.objects.all()) # serializers.CharField(source='EventType.id', read_only=True)
#    Owner_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Event
        fields = ('id', 'Theme_id', 'ExpositionTitle', 'HasPoster', 'HasPhotos', 'StartDate', 'EndDate', 'Title', 'Description', 'Author', 'Location', 'VisitorCount', 'ChildVisitorCount', 'JuniorVisitorCount', 'BooksOnDisplayCount', 'IssuedBooksCount', 'Department_id', 'EventForm_id', 'EventType_id', 'Owner_id')
    
    def create(self, validated_data):
        id_department = validated_data.pop('Department_id')
        print('create event: id_department=',id_department)
        id_theme = validated_data.pop('Theme_id')
        print('create event: id_theme=',id_theme)
        id_eventform = validated_data.pop('EventForm_id')
        print('create event: id_eventform=',id_eventform)
        id_eventtype = validated_data.pop('EventType_id')
        print('create event: id_eventtype=',id_eventtype)

        department = Department.objects.get_or_create(id=id_department)[0]

        theme = Theme.objects.get_or_create(id=id_theme)[0]
        eventform = EventForm.objects.get_or_create(id=id_eventform)[0]
        eventtype = EventType.objects.get_or_create(id=id_eventtype)[0]
        event = Event.objtects.create(Department_id=Department.id, Theme_id=id_theme,EventForm_id=id_eventform,EventType_id=id_eventtype)
        return event
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
