# Generated by Django 3.2.18 on 2023-02-27 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_alter_docotrs_dep_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docotrs',
            old_name='dep_id',
            new_name='department',
        ),
    ]
