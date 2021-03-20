# Generated by Django 3.1.4 on 2021-03-20 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='count',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(default='NEW', verbose_name=[('NEW', 'Получен'), ('IN_PROGRESS', 'Выполняется'), ('DONE', 'Готов'), ('CANCELLED', 'Отменён')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(editable=False),
        ),
    ]
