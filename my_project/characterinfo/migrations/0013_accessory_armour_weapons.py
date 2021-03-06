# Generated by Django 2.1.7 on 2019-03-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characterinfo', '0012_auto_20190302_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('minLevel', models.IntegerField(default=1)),
                ('bonusType1', models.CharField(max_length=100, null=True)),
                ('bonus1', models.IntegerField(default=1)),
                ('bonusType2', models.CharField(max_length=100, null=True)),
                ('bonus2', models.IntegerField(default=1)),
                ('bonusType3', models.CharField(max_length=100, null=True)),
                ('bonus3', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Armour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('minLevel', models.IntegerField(default=1)),
                ('pdBonus', models.IntegerField(default=1)),
                ('mdBonus', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Weapons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('minLevel', models.IntegerField(default=1)),
                ('paBonus', models.IntegerField(default=1)),
                ('maBonus', models.IntegerField(default=1)),
            ],
        ),
    ]
