# Generated by Django 4.0.2 on 2022-02-02 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_productcolour_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productcolour',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='product.productcolour'),
        ),
        migrations.AddField(
            model_name='product',
            name='productsize',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='product.productsize'),
        ),
    ]
