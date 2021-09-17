# Generated by Django 3.2.7 on 2021-09-16 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dlt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
