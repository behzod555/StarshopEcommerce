# Generated by Django 3.2.5 on 2021-09-03 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20210903_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
    ]
