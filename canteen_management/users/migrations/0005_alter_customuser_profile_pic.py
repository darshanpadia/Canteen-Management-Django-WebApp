# Generated by Django 4.2 on 2024-02-29 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/blank-profile-pic.jpg', upload_to='profile_pics/'),
        ),
    ]