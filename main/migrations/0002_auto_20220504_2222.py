# Generated by Django 3.2 on 2022-05-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
