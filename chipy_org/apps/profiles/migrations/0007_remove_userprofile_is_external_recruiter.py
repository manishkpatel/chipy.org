# Generated by Django 2.2.12 on 2020-07-30 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20200730_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_external_recruiter',
        ),
    ]