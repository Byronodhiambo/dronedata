# Generated by Django 4.1.3 on 2022-11-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='airframe_hrs',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flights',
            name='flight_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rpas',
            name='airframe_bf',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
