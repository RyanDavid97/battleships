# Generated by Django 2.1.1 on 2019-03-25 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('maximum_x', models.IntegerField(default=30)),
                ('maximum_y', models.IntegerField(default=30)),
                ('ships_per_person', models.IntegerField(default=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battleships.Game')),
                ('locations', models.ManyToManyField(to='battleships.Location')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battleships.Player')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(to='battleships.Player'),
        ),
        migrations.AddField(
            model_name='action',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battleships.Game'),
        ),
        migrations.AddField(
            model_name='action',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battleships.Location'),
        ),
        migrations.AddField(
            model_name='action',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battleships.Player'),
        ),
    ]
