# Generated by Django 4.1.1 on 2022-09-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Цена'),
        ),
    ]
