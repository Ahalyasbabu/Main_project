# Generated by Django 3.2.18 on 2023-02-26 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0007_departments_dep_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departments',
            name='dep_id',
        ),
    ]
