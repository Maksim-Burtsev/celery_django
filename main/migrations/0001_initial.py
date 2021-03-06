# Generated by Django 3.2 on 2022-05-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('views', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
