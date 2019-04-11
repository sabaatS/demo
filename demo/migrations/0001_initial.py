# Generated by Django 2.1.7 on 2019-04-09 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100)),
                ('singer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('album_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Album')),
            ],
        ),
    ]
