# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class EventType(models.Model):
    title = models.CharField(max_length=255)

class Department(models.Model):
    title = models.CharField(max_length=255)

class EventForm(models.Model):
    title = models.CharField(max_length=255)

class Theme(models.Model):
    title = models.CharField(max_length=255)

class Event(models.Model):
    EventType = models.ForeignKey('EventType', models.SET_NULL, verbose_name='Тип мероприятия',help_text='Массовое мероприятие')
    Department =models.ForeignKey('Department', models.SET_NULL, verbose_name='Отдел-организатор',help_text='Выберите из списка')
    EventForm = models.ForeignKey('EventForm', models.SET_NULL, verbose_name='',help_text='Выберите из списка')
    Owner = models.ForeignKey(get_user_model(), models.SET_NULL, verbose_name='Оператор')
    Theme = models.ForeignKey('Theme', models.SET_NULL, verbose_name='Тема мероприятия',help_text='Выберите из списка')
    ExpositionTitle = models.CharField(max_length=255, verbose_name='Название сопровождающей выставки',help_text='Введите название выставки')
    HasPoster = models.BooleanField(default=False, verbose_name='Была ли подготовлена афиша?')
    HasPhotos = models.BooleanField(default=False, verbose_name='Место хранения медиа-отчета') # TODO: что тут? строка или полу есть ли фото???
    StartDate = models.DateTimeField(verbose_name='Начало мероприятия')
    EndDate = models.DateTimeField(verbose_name='Окончание мероприятия')
    Title = models.CharField(max_length=255, verbose_name='Название мероприятия',help_text='Введите название мероприятия')
    Description = models.TextField(verbose_name='Описание содержания мероприятия',help_text='Опишите мероприятие')
    Author = models.CharField(max_length=255, verbose_name='Регистратор мероприятия',help_text='ФИО оператора, по данным авторизации')
    Location = models.CharField(max_length=255, verbose_name='Место провидения',help_text='Двор, усадьба, улица и etc.')
    VisitorCount = models.IntegerField(verbose_name='Количество участников')
    ChildVisitorCount = models.IntegerField(verbose_name='.. из них детей 14 лет')
    JuniorVisitorCount = models.IntegerField(verbose_name='..от 14 до 18 лет')
    BooksOnDisplayCount = models.IntegerField(verbose_name='Количество выставвленых книг')
    IssuedBooksCount = models.IntegerField(verbose_name='Количество выданных книг')

