# Generated by Django 4.1.7 on 2023-04-06 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='date_published',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 4, 6, 18, 49, 16, 685470, tzinfo=datetime.timezone.utc)),
        ),
    ]
