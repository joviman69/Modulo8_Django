# Generated by Django 2.0.6 on 2018-07-04 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_post_publish_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish_date',
        ),
        migrations.AddField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 4, 10, 40, 53, 522028)),
        ),
    ]
