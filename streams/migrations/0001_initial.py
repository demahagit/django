# Generated by Django 2.1.8 on 2019-05-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(help_text='location tag', max_length=100)),
            ],
            options={
                'verbose_name': 'Location Tag',
                'verbose_name_plural': 'Location Tags',
            },
        ),
        migrations.CreateModel(
            name='TripType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_type', models.CharField(help_text='location tag', max_length=100)),
            ],
            options={
                'verbose_name': 'Trip Type',
                'verbose_name_plural': 'Trip Types',
            },
        ),
    ]
