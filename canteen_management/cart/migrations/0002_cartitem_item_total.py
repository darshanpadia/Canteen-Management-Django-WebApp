# Generated by Django 4.2 on 2024-04-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='item_total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
