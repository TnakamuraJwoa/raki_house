# Generated by Django 3.2.7 on 2022-01-17 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0013_rename_set_date_room_in_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='in_date',
        ),
        migrations.AddField(
            model_name='room',
            name='set_date',
            field=models.DateField(blank=True, null=True, verbose_name='いつまでに'),
        ),
        migrations.AddField(
            model_name='room',
            name='task',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='やること'),
        ),
    ]
