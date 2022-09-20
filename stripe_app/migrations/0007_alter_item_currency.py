# Generated by Django 4.1.1 on 2022-09-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_app', '0006_tax_order_order_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('USD', 'usd'), ('JPY', 'jpy'), ('AUD', 'aud')], default='USD', max_length=50, verbose_name='Валюта'),
        ),
    ]