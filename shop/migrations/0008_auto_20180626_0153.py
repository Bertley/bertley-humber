# Generated by Django 2.0.5 on 2018-06-26 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20180626_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Ref_Product_type'),
        ),
    ]
