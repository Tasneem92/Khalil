# Generated by Django 2.1.1 on 2018-09-27 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_order', models.IntegerField()),
                ('orderedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic_app.UserProfileInfo')),
            ],
        ),
    ]
