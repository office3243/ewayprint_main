# Generated by Django 2.0 on 2019-06-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_transaction_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_show',
            field=models.BooleanField(default=True),
        ),
    ]
