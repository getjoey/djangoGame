# Generated by Django 2.1.7 on 2019-03-03 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characterinfo', '0023_position_posy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characterinfo.Character'),
        ),
    ]
