# Generated by Django 2.0.4 on 2018-04-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acce_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=10)),
                ('data_x', models.CharField(max_length=3)),
                ('data_y', models.CharField(max_length=3)),
                ('data_z', models.CharField(max_length=3)),
                ('data', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]