# Generated by Django 3.2.18 on 2023-03-08 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_appointmentsmdel_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentsmdel',
            name='approved',
        ),
    ]
