# Generated by Django 4.2.4 on 2023-08-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cruds_App', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Image',
            field=models.ImageField(default='def.png', upload_to='Prof_pic/'),
        ),
    ]
