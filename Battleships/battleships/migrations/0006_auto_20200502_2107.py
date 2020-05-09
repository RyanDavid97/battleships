# Generated by Django 3.0.2 on 2020-05-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0005_auto_20190402_2155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='ship',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='ship',
            name='hp',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='game',
            name='maximum_x',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='game',
            name='maximum_y',
            field=models.IntegerField(default=15),
        ),
    ]
