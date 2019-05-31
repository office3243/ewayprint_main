# Generated by Django 2.0 on 2019-05-30 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txnid', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_info', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('gateway', models.CharField(choices=[('PAYU', 'Payumoney')], default='PAYU', max_length=5)),
                ('status', models.CharField(choices=[('IN', 'Initiated'), ('SC', 'Success'), ('FL', 'Failed'), ('HD', 'Hold')], default='IN', max_length=2)),
            ],
        ),
    ]
