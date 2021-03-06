# Generated by Django 3.1.4 on 2020-12-13 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Отдел')),
            ],
        ),
        migrations.CreateModel(
            name='EventForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Форма мероприятия')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тип мероприятия')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Тема мероприятия')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExpositionTitle', models.CharField(help_text='Введите название выставки', max_length=255, verbose_name='Название сопровождающей выставки')),
                ('HasPoster', models.BooleanField(default=False, verbose_name='Была ли подготовлена афиша?')),
                ('HasPhotos', models.BooleanField(default=False, verbose_name='Место хранения медиа-отчета')),
                ('StartDate', models.DateTimeField(verbose_name='Начало мероприятия')),
                ('EndDate', models.DateTimeField(verbose_name='Окончание мероприятия')),
                ('Title', models.CharField(help_text='Введите название мероприятия', max_length=255, verbose_name='Название мероприятия')),
                ('Description', models.TextField(help_text='Опишите мероприятие', verbose_name='Описание содержания мероприятия')),
                ('Author', models.CharField(help_text='ФИО оператора, по данным авторизации', max_length=255, verbose_name='Регистратор мероприятия')),
                ('Location', models.CharField(help_text='Двор, усадьба, улица и etc.', max_length=255, verbose_name='Место провидения')),
                ('VisitorCount', models.IntegerField(verbose_name='Количество участников')),
                ('ChildVisitorCount', models.IntegerField(verbose_name='.. из них детей 14 лет')),
                ('JuniorVisitorCount', models.IntegerField(verbose_name='..от 14 до 18 лет')),
                ('BooksOnDisplayCount', models.IntegerField(verbose_name='Количество выставвленых книг')),
                ('IssuedBooksCount', models.IntegerField(verbose_name='Количество выданных книг')),
                ('Department', models.ForeignKey(help_text='Выберите из списка', on_delete=django.db.models.deletion.CASCADE, to='sounbs_api.department', verbose_name='Отдел-организатор')),
                ('EventForm', models.ForeignKey(help_text='Выберите из списка', on_delete=django.db.models.deletion.CASCADE, to='sounbs_api.eventform', verbose_name='')),
                ('EventType', models.ForeignKey(help_text='Массовое мероприятие', on_delete=django.db.models.deletion.CASCADE, to='sounbs_api.eventtype', verbose_name='Тип мероприятия')),
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Оператор')),
                ('Theme', models.ForeignKey(help_text='Выберите из списка', on_delete=django.db.models.deletion.CASCADE, to='sounbs_api.theme', verbose_name='Тема мероприятия')),
            ],
        ),
    ]
