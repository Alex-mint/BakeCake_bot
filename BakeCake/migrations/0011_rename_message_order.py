# Generated by Django 3.2.8 on 2021-10-28 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BakeCake', '0010_auto_20211027_1820'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='Order',
        ),
    ]
