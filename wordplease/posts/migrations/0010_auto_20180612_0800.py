# Generated by Django 2.0.6 on 2018-06-12 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='topic',
            new_name='theme',
        ),
    ]
