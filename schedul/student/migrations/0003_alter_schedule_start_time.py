# Generated by Django 4.2.16 on 2024-10-17 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_subject_alter_schedule_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
