# Generated by Django 3.2.7 on 2021-09-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='facebook',
            field=models.URLField(default='Email'),
        ),
        migrations.AddField(
            model_name='game',
            name='website',
            field=models.URLField(default='Email', max_length=100),
        ),
    ]
