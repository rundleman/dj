# Generated by Django 2.2.2 on 2019-11-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='request_status',
            field=models.IntegerField(choices=[(1, 'Создана'), (2, 'Назначена'), (3, 'В работе'), (4, 'Выполнена')], default=0, verbose_name='Статус заявки'),
            preserve_default=False,
        ),
    ]
