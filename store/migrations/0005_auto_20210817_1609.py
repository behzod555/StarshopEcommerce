# Generated by Django 3.2.5 on 2021-08-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210817_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Телефоны',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('бытовая техника', 'Бытовая техника'), ('климатическая техника', 'Климатическая техника'), ('компьютерная техника', 'Компьютерная техника'), ('мужские туфли', 'Мужские туфли'), ('спортивные товары', 'Спортивные товары'), ('телевизоры', 'Телевизоры'), ('телефоны', 'Телефоны')], default='Категория', max_length=300)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='color',
            field=models.CharField(choices=[('бытовая техника', 'Бытовая техника'), ('климатическая техника', 'Климатическая техника'), ('компьютерная техника', 'Компьютерная техника'), ('мужские туфли', 'Мужские туфли'), ('спортивные товары', 'Спортивные товары'), ('телевизоры', 'Телевизоры'), ('телефоны', 'Телефоны')], default='green', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('бытовая техника', 'Бытовая техника'), ('климатическая техника', 'Климатическая техника'), ('компьютерная техника', 'Компьютерная техника'), ('мужские туфли', 'Мужские туфли'), ('спортивные товары', 'Спортивные товары'), ('телевизоры', 'Телевизоры'), ('телефоны', 'Телефоны')], default='Категория', max_length=300),
        ),
    ]
