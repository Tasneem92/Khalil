# Generated by Django 2.1.1 on 2018-09-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_auto_20180930_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.CharField(max_length=256, verbose_name={}),
        ),
    ]
