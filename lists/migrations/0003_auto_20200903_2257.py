# Generated by Django 2.2.5 on 2020-09-03 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20200901_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='room',
            new_name='rooms',
        ),
    ]
