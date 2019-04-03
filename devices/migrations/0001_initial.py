# Generated by Django 2.1.4 on 2019-04-02 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='deviceId')),
                ('name', models.CharField(max_length=512, verbose_name='deviceName')),
                ('code', models.CharField(max_length=256, verbose_name='deviceCode')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='createTime')),
                ('modify_time', models.DateTimeField(auto_now_add=True, verbose_name='modifyTime')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.Partners', verbose_name='partner')),
            ],
            options={
                'verbose_name': 'device',
                'verbose_name_plural': 'device',
                'ordering': ['uid'],
            },
        ),
        migrations.CreateModel(
            name='DevicesType',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='deviceTypeId')),
                ('name', models.CharField(max_length=512, verbose_name='devicesType')),
                ('des', models.CharField(blank=True, max_length=1024, null=True, verbose_name='des')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='createTime')),
                ('modify_time', models.DateTimeField(auto_now_add=True, verbose_name='modifyTime')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'devicesType',
                'verbose_name_plural': 'devicesType',
                'ordering': ['uid'],
            },
        ),
        migrations.AddField(
            model_name='devices',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.DevicesType', verbose_name='devicesType'),
        ),
        migrations.AddField(
            model_name='devices',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
