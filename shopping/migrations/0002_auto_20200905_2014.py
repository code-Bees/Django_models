# Generated by Django 3.1 on 2020-09-05 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(max_length=100),
        ),
    ]
