# Generated by Django 3.1 on 2020-09-29 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0023_auto_20200929_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=255, verbose_name='商品')),
            ],
        ),
        migrations.AlterField(
            model_name='menucategory',
            name='category_name',
            field=models.CharField(max_length=255, verbose_name='カテゴリ'),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.menucategory'),
        ),
    ]
