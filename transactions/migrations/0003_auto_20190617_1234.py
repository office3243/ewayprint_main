# Generated by Django 2.0 on 2019-06-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20190613_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='paper_type',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='file',
            field=models.FileField(upload_to='transactions/transaction_files/2019-06-17/'),
        ),
    ]
