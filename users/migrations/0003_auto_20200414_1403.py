# Generated by Django 3.0.5 on 2020-04-14 14:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_connections'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='internships',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=100), null=True, size=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=100), null=True, size=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=2), null=True, size=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None),
        ),
    ]
