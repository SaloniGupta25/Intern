# Generated by Django 3.1.4 on 2020-12-26 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_hotel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='name',
            new_name='Bio',
        ),
    ]
