# Generated by Django 5.0.3 on 2024-03-31 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
    ]
