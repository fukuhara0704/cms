# Generated by Django 3.1 on 2020-09-29 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20200929_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=255, verbose_name='メニュー名')),
            ],
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='category_name',
            field=models.CharField(max_length=255, verbose_name='カテゴリ名'),
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.AddField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.menucategory'),
        ),
    ]