# Generated by Django 3.1.4 on 2020-12-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20201226_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_Main_Img',
            field=models.ImageField(upload_to='profile_pic/'),
        ),
    ]
