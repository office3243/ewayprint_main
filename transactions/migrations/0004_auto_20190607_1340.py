# Generated by Django 2.0 on 2019-06-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20190604_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='file',
            field=models.FileField(upload_to='transactions/transaction_files/2019-06-07/'),
        ),
    ]
