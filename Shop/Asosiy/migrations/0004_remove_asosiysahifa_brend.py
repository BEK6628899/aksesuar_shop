# Generated by Django 5.0 on 2023-12-23 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0003_alter_asosiysahifa_narx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asosiysahifa',
            name='brend',
        ),
    ]