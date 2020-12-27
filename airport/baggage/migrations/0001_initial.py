# Generated by Django 2.2.7 on 2019-11-24 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('passenger', '0001_initial'),
        ('postlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='baggage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=8, unique=True)),
                ('fl_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bag_flno', to='postlog.FlightNum')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bag_name', to='passenger.passenger')),
                ('pnr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bag_pnr', to='passenger.pnr')),
            ],
        ),
    ]
