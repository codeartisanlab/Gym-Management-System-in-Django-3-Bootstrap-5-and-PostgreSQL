# Generated by Django 3.2 on 2021-08-12 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_notify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notify',
            name='status',
        ),
    ]
