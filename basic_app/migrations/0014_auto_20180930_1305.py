# Generated by Django 2.1.1 on 2018-09-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0013_auto_20180930_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='basic_app.Address'),
        ),
    ]
