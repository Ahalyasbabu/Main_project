# Generated by Django 3.2.18 on 2023-02-26 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0004_alter_departments_departments_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='departments_id',
            new_name='dep_id',
        ),
    ]
