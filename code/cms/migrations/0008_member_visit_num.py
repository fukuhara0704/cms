# Generated by Django 3.0.9 on 2020-08-15 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20200815_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='visit_num',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='来店回数'),
        ),
    ]