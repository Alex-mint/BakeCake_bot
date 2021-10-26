# Generated by Django 3.2.8 on 2021-10-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakeCake', '0002_alter_profile_external_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='berries',
            field=models.TextField(blank=True, verbose_name='Ягоды'),
        ),
        migrations.AddField(
            model_name='profile',
            name='decor',
            field=models.TextField(blank=True, verbose_name='Декор'),
        ),
        migrations.AddField(
            model_name='profile',
            name='form',
            field=models.TextField(blank=True, verbose_name='Форма'),
        ),
        migrations.AddField(
            model_name='profile',
            name='number_levels',
            field=models.TextField(blank=True, verbose_name='Количество уровней'),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.TextField(blank=True, verbose_name='Надпись'),
        ),
        migrations.AddField(
            model_name='profile',
            name='topping',
            field=models.TextField(blank=True, verbose_name='Топпинг'),
        ),
    ]
