# Generated by Django 3.2.8 on 2021-10-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_entry',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
