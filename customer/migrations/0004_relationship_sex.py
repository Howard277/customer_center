# Generated by Django 2.1 on 2018-12-11 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_photo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='sex',
            field=models.BooleanField(default=True),
        ),
    ]
