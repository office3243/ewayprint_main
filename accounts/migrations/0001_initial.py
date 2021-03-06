# Generated by Django 2.0 on 2019-06-25 07:49

import accounts.managers
import accounts.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone', models.CharField(max_length=13, unique=True, validators=[accounts.validators.phone_number_validator], verbose_name='phone number')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('phone_verified', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=32, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=32, verbose_name='last name')),
                ('city', models.CharField(blank=True, default='Pune', max_length=30, verbose_name='city')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
    ]
