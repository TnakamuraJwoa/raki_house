# Generated by Django 3.2.7 on 2022-02-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220207_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='member_type',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='メンバータイプ'),
        ),
    ]
