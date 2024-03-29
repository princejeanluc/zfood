# Generated by Django 5.0.1 on 2024-03-02 10:44

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='zfood/static/association_upload')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('delegation', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='zfood/static/user_upload')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='zfood/static/store_upload')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zfoodapi.client')),
            ],
        ),
        migrations.CreateModel(
            name='bouquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zfoodapi.command')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='zfood/static/product_upload')),
                ('expiration_date', models.DateTimeField(default=datetime.datetime(2024, 3, 2, 10, 44, 31, 341311, tzinfo=datetime.timezone.utc))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('association', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zfoodapi.association')),
                ('bouquet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zfoodapi.bouquet')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zfoodapi.store')),
            ],
        ),
    ]
