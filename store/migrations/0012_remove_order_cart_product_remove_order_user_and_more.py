# Generated by Django 4.2.8 on 2023-12-26 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_cardproduct_remove_order_items_delete_orderitem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='CardProduct',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
