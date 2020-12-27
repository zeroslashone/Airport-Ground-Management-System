# Generated by Django 2.2.7 on 2019-11-24 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('postlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('crewid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
                ('crew_dob', models.DateField()),
                ('role', models.CharField(max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='al1', to='postlog.Airline')),
            ],
        ),
    ]
