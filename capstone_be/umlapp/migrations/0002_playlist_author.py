# Generated by Django 3.1.8 on 2021-06-27 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umlapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='author',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='umlapp.user'),
        ),
    ]