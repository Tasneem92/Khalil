# Generated by Django 2.1.1 on 2018-09-30 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0014_auto_20180930_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Address'),
        ),
    ]