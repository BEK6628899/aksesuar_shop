# Generated by Django 5.0 on 2024-01-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0012_asosiysahifa_malumot'),
    ]

    operations = [
        migrations.AddField(
            model_name='asosiysahifa',
            name='rang',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
