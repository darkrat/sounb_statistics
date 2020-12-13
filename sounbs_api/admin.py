# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import EventType, EventForm, Department, Theme, Event
# Register your models here.
admin.site.register(Event)
admin.site.register(EventForm)
admin.site.register(EventType)
admin.site.register(Department)
admin.site.register(Theme)

