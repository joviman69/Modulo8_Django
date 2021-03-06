# Generated by Django 2.0.6 on 2018-06-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
