# Generated by Django 3.2.6 on 2021-08-26 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]