# Generated by Django 4.2.1 on 2024-04-11 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_total_price_productinorder_nmb_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Товар в заказе', 'verbose_name_plural': 'Товары в заказе'},
        ),
    ]
