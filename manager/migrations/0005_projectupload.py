# Generated by Django 5.0.3 on 2024-03-31 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_remove_task_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectUpload',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manager.task')),
            ],
        ),
    ]
