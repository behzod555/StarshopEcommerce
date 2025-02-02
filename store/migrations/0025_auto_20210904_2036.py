# Generated by Django 3.2.5 on 2021-09-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_remove_product_digital'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tel',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='familiya',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='imya',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='tel',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='novinki',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='popularnye',
            field=models.BooleanField(default=False),
        ),
    ]
