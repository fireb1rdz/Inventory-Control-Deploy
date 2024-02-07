# Generated by Django 5.0.1 on 2024-01-30 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_product_name_alter_product_suppliers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('local', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', unique=True)),
            ],
        ),
    ]
