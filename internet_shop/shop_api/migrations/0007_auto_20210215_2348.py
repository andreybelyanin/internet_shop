# Generated by Django 3.1.5 on 2021-02-15 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0006_auto_20210215_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourites',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='favorites',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop_api.favourites', verbose_name='Избранное'),
        ),
    ]