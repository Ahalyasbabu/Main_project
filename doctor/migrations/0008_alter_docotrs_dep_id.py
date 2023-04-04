# Generated by Django 3.2.18 on 2023-02-26 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0007_departments_dep_id'),
        ('doctor', '0007_docotrs_dep_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docotrs',
            name='dep_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departments.departments'),
        ),
    ]