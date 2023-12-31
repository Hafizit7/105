# Generated by Django 4.2.8 on 2023-12-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_category_parent_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.PositiveIntegerField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(max_length=30),
        ),
    ]
