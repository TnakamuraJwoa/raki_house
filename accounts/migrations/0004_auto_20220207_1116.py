# Generated by Django 3.2.7 on 2022-02-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_member_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.IntegerField(blank=True, null=True, verbose_name='性別'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='member_type',
            field=models.IntegerField(blank=True, null=True, verbose_name='メンバータイプ'),
        ),
    ]
