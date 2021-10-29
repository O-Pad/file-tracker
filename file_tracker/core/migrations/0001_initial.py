# Generated by Django 3.2.8 on 2021-10-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=15)),
                ('port', models.CharField(max_length=4)),
                ('user_id', models.CharField(max_length=200)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
