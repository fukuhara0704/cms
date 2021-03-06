# Generated by Django 3.0.9 on 2020-08-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='名前')),
                ('name_read', models.CharField(blank=True, max_length=255, null=True, verbose_name='フリガナ')),
                ('gender', models.IntegerField(blank=True, choices=[(1, '男性'), (2, '女性'), (3, 'その他')], null=True, verbose_name='性別')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='誕生日')),
                ('email', models.EmailField(blank=True, max_length=256, null=True, verbose_name='メールアドレス')),
                ('telephone', models.CharField(blank=True, max_length=100, null=True, verbose_name='電話番号')),
                ('house', models.CharField(blank=True, max_length=100, null=True, verbose_name='建物名')),
                ('address_line1', models.CharField(blank=True, max_length=100, null=True, verbose_name='住所2')),
                ('address_line2', models.CharField(blank=True, max_length=100, null=True, verbose_name='住所1')),
                ('zip_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='郵便番号')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成時間')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
            ],
        ),
    ]
