# Generated by Django 5.0.5 on 2024-05-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('marks', models.FloatField()),
            ],
        ),
    ]
