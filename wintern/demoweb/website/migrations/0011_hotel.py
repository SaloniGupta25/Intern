# Generated by Django 3.1.4 on 2020-12-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('hotel_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
