# Generated by Django 5.0 on 2023-12-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0002_rename_index_asosiysahifa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asosiysahifa',
            name='narx',
            field=models.FloatField(),
        ),
    ]
