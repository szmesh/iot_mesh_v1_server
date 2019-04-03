# Generated by Django 2.1.4 on 2019-04-02 08:45

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
            name='Area',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='areaId')),
                ('name', models.CharField(error_messages={'blank': 'blankEMAreaName', 'invalid': 'invalidEMAreaName', 'invalid_choice': 'invalidChoiceEMAreaName', 'null': 'nullEMAreaName', 'unique': 'uniqueEMAreaName'}, help_text='helpTextAreaName', max_length=512, verbose_name='areaName')),
                ('code', models.CharField(max_length=256, unique=True, verbose_name='areaCode')),
                ('level', models.IntegerField(choices=[(1000, 'continent'), (2000, 'country'), (3000, 'province'), (4000, 'city'), (5000, 'zone')], default=1000, error_messages={'blank': 'blankEMLevel', 'invalid': 'invalidEMLevel', 'invalid_choice': 'invalidChoiceEMLevel', 'null': 'nullEMLevel', 'unique': 'uniqueEMLevel'}, help_text='helpTextLevel', verbose_name='areaLevel')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='createTime')),
                ('modify_time', models.DateTimeField(auto_now_add=True, verbose_name='modifyTime')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='area.Area', verbose_name='parent')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'area',
                'verbose_name_plural': 'area',
                'ordering': ['uid'],
            },
        ),
        migrations.CreateModel(
            name='CityArea',
            fields=[
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'city',
                'proxy': True,
                'indexes': [],
            },
            bases=('area.area',),
        ),
        migrations.CreateModel(
            name='ContinentArea',
            fields=[
            ],
            options={
                'verbose_name': 'continent',
                'verbose_name_plural': 'continent',
                'proxy': True,
                'indexes': [],
            },
            bases=('area.area',),
        ),
        migrations.CreateModel(
            name='CountryArea',
            fields=[
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'country',
                'proxy': True,
                'indexes': [],
            },
            bases=('area.area',),
        ),
        migrations.CreateModel(
            name='ProvinceArea',
            fields=[
            ],
            options={
                'verbose_name': 'province',
                'verbose_name_plural': 'province',
                'proxy': True,
                'indexes': [],
            },
            bases=('area.area',),
        ),
        migrations.CreateModel(
            name='ZoneArea',
            fields=[
            ],
            options={
                'verbose_name': 'zone',
                'verbose_name_plural': 'zone',
                'proxy': True,
                'indexes': [],
            },
            bases=('area.area',),
        ),
    ]
