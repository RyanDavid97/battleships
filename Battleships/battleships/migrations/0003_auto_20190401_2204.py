# Generated by Django 2.1.1 on 2019-04-01 22:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0002_location_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='action',
            name='result',
            field=models.CharField(max_length=100),
        ),
    ]
