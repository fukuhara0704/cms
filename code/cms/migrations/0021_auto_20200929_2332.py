# Generated by Django 3.1 on 2020-09-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuDesert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desert_name', models.CharField(max_length=255, verbose_name='デザート名')),
            ],
        ),
        migrations.CreateModel(
            name='MenuDrink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(max_length=255, verbose_name='ドリンク名')),
            ],
        ),
        migrations.CreateModel(
            name='MenuMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_name', models.CharField(max_length=255, verbose_name='メイン名')),
            ],
        ),
        migrations.CreateModel(
            name='MenuZensai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zensai_name', models.CharField(max_length=255, verbose_name='前菜名')),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='MenuCategory',
        ),
    ]
