# Generated by Django 2.0 on 2019-06-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='file',
            field=models.FileField(upload_to='transactions/transaction_files/2019-06-01/'),
        ),
    ]