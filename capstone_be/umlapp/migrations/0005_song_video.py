# Generated by Django 3.1.8 on 2021-07-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('umlapp', '0004_auto_20210629_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='video',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
