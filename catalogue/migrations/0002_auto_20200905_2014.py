# Generated by Django 3.1 on 2020-09-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='productsupplier',
            name='street_address',
            field=models.CharField(max_length=200),
        ),
    ]
