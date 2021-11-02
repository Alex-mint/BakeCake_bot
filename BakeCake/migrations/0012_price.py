# Generated by Django 3.2.8 on 2021-10-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakeCake', '0011_rename_message_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_1', models.IntegerField(blank=True, verbose_name='1 уровень')),
                ('level_2', models.IntegerField(blank=True, verbose_name='2 уровень')),
                ('level_3', models.IntegerField(blank=True, verbose_name='3 уровень')),
                ('square', models.IntegerField(blank=True, verbose_name='Квадрат')),
                ('circle', models.IntegerField(blank=True, verbose_name='Круг')),
                ('rectangle', models.IntegerField(blank=True, verbose_name='Прямоугольник')),
                ('white_syrup', models.IntegerField(blank=True, verbose_name='Белый сироп')),
                ('caramel_syrup', models.IntegerField(blank=True, verbose_name='Карамельный сироп')),
                ('maple_syrup', models.IntegerField(blank=True, verbose_name='Кленовый сироп')),
                ('strawberry_syrup', models.IntegerField(blank=True, verbose_name='Клубничный сироп')),
                ('blueberry_syrup', models.IntegerField(blank=True, verbose_name='Черничный сироп')),
                ('milk_chocolate', models.IntegerField(blank=True, verbose_name='Молочный шоколад')),
                ('blackberry', models.IntegerField(blank=True, verbose_name='Ежевика')),
                ('raspberry', models.IntegerField(blank=True, verbose_name='Малина')),
                ('blueberry', models.IntegerField(blank=True, verbose_name='Голубика')),
                ('strawberry', models.IntegerField(blank=True, null=True, verbose_name='Клубника ')),
                ('pistachios', models.IntegerField(blank=True, verbose_name='Фисташки')),
                ('meringue', models.IntegerField(blank=True, null=True, verbose_name='Безе')),
                ('hazelnuts', models.IntegerField(blank=True, verbose_name='Фундук')),
                ('pecan', models.IntegerField(blank=True, verbose_name='Пекан')),
                ('marshmallow', models.IntegerField(blank=True, verbose_name='Маршмеллоу')),
                ('marzipan', models.IntegerField(blank=True, verbose_name='Марципан')),
                ('title', models.IntegerField(blank=True, verbose_name='Надпись')),
            ],
            options={
                'verbose_name': 'Цены',
                'verbose_name_plural': 'Цены',
            },
        ),
    ]