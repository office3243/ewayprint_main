# Generated by Django 2.0 on 2019-06-13 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='details',
        ),
        migrations.AddField(
            model_name='transaction',
            name='refrence',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='file',
            field=models.FileField(upload_to='transactions/transaction_files/2019-06-13/'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='station_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stations.StationClass'),
        ),
    ]