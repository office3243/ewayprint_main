# Generated by Django 2.0 on 2019-06-24 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_auto_20190622_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='uuid',
            field=models.UUIDField(unique=True),
        ),
    ]
