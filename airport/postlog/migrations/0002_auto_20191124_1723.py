# Generated by Django 2.2.7 on 2019-11-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='airline',
            field=models.CharField(max_length=35),
        ),
    ]
