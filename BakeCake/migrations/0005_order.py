# Generated by Django 3.2.8 on 2021-10-26 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BakeCake', '0004_profile_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BakeCake.profile', verbose_name='Профиль')),
            ],
        ),
    ]
