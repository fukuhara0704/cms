# Generated by Django 3.0.9 on 2020-08-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_member_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='性別'),
        ),
    ]
