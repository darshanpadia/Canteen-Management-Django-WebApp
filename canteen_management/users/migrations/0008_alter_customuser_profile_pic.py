# Generated by Django 4.2 on 2024-03-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_somaiya_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/blank-product.png', upload_to='profile_pics/'),
        ),
    ]
