# Generated by Django 4.0.3 on 2022-04-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMundial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sede',
            name='ciudad_sede',
            field=models.CharField(max_length=20),
        ),
    ]
