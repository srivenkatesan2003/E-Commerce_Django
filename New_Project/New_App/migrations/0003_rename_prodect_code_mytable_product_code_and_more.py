# Generated by Django 4.2.13 on 2024-06-18 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('New_App', '0002_mytable_food_product_mytable_gst_mytable_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mytable',
            old_name='prodect_code',
            new_name='product_code',
        ),
        migrations.RenameField(
            model_name='mytable',
            old_name='prodect_name',
            new_name='product_name',
        ),
    ]
