# Generated by Django 2.0.6 on 2018-06-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_post_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.CharField(choices=[('UND', 'Undefined'), ('TEC', 'Technology'), ('INT', 'Internet'), ('SCI', 'Science'), ('MOV', 'Movies'), ('TV', 'TV'), ('SPO', 'Sports'), ('GAM', 'Games')], default='UND', max_length=3),
        ),
    ]