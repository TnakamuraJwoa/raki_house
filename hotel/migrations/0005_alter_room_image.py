# Generated by Django 3.2.7 on 2022-02-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_room_futon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='部屋画像メイン'),
        ),
    ]
