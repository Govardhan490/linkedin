# Generated by Django 3.0.5 on 2020-04-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='connections',
            field=models.ManyToManyField(to='users.Profile'),
        ),
    ]