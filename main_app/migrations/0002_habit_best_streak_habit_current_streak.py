# Generated by Django 4.2.7 on 2023-11-06 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='best_streak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='habit',
            name='current_streak',
            field=models.IntegerField(default=0),
        ),
    ]
