# Generated by Django 4.1.3 on 2022-11-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='new',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='old_price',
            field=models.CharField(blank=True, default=2, max_length=10),
            preserve_default=False,
        ),
    ]