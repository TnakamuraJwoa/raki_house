# Generated by Django 3.2.7 on 2022-01-17 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0018_auto_20220117_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='set_date',
            new_name='in_date',
        ),
        migrations.RemoveField(
            model_name='room',
            name='task',
        ),
    ]
