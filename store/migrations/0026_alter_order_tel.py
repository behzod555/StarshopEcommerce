# Generated by Django 3.2.5 on 2021-09-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20210904_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tel',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
