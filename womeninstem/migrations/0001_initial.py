# Generated by Django 3.2.4 on 2021-11-13 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('work', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
                ('achieve', models.CharField(max_length=500)),
            ],
        ),
    ]
