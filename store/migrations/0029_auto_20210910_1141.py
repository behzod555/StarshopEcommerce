# Generated by Django 3.2.5 on 2021-09-10 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Клиенты', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказы', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Заказанные товары', 'verbose_name_plural': 'Заказанные товары'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукты', 'verbose_name_plural': 'Продукты'},
        ),
    ]
