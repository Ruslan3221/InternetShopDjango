# Generated by Django 5.0.4 on 2024-06-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_telegramid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='Описание', max_length=1000),
        ),
    ]