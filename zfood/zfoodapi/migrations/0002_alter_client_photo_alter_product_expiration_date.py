# Generated by Django 5.0.1 on 2024-03-02 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zfoodapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.FileField(upload_to='zfood/static/user_upload'),
        ),
        migrations.AlterField(
            model_name='product',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 2, 13, 49, 52, 863231, tzinfo=datetime.timezone.utc)),
        ),
    ]