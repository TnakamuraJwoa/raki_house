# Generated by Django 3.2.7 on 2022-02-07 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20220207_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='Ticket_number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotel.ticket'),
            preserve_default=False,
        ),
    ]
