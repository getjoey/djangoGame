# Generated by Django 2.1.7 on 2019-03-01 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characterinfo', '0007_character_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='username',
        ),
    ]
