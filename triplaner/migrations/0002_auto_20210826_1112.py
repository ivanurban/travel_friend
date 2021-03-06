# Generated by Django 3.2.6 on 2021-08-26 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('triplaner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='from_destination',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
