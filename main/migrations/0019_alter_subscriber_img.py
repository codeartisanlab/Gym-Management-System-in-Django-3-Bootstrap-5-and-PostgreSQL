# Generated by Django 3.2 on 2021-08-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_subscriber_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='img',
            field=models.ImageField(null=True, upload_to='subs/'),
        ),
    ]
