# Generated by Django 2.0 on 2019-05-18 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_recharge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='recharge',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='recharges.Recharge'),
        ),
    ]
