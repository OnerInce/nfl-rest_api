# Generated by Django 3.1.4 on 2021-01-03 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nfl_id', models.IntegerField()),
                ('display_name', models.CharField(max_length=100)),
                ('jersey_number', models.IntegerField()),
                ('height', models.CharField(max_length=10)),
                ('weight', models.IntegerField()),
                ('birth_date', models.CharField(max_length=50)),
                ('season', models.IntegerField()),
                ('college_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='players.college')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='players.position')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='players.team')),
            ],
        ),
    ]
