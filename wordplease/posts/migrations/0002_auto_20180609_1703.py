# Generated by Django 2.0.6 on 2018-06-09 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='blog',
            new_name='posts',
        ),
    ]