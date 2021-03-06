# Generated by Django 3.1 on 2020-08-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_member_visit_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='int_gender',
        ),
        migrations.AddField(
            model_name='member',
            name='latest_visit_day',
            field=models.DateField(blank=True, null=True, verbose_name=' 直近の来店日'),
        ),
        migrations.AddField(
            model_name='member',
            name='prefectures',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='都道府県'),
        ),
        migrations.AlterField(
            model_name='member',
            name='address_line1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='住所1'),
        ),
        migrations.AlterField(
            model_name='member',
            name='address_line2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='住所2'),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, '男性'), (2, '女性'), (3, 'その他')], null=True, verbose_name='性別'),
        ),
    ]
