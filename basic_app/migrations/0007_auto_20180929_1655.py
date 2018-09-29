# Generated by Django 2.1.1 on 2018-09-29 16:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_app', '0006_userorders_orderedby'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('line1', models.CharField(max_length=255)),
                ('line2', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=14)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date_placed', models.DateTimeField(db_index=True, default=datetime.datetime.now)),
                ('delivery_date', models.DateTimeField(db_index=True)),
                ('total_incl_delivery', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.Address')),
                ('orderedBy', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userorders',
            name='orderedBy',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserOrders',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]