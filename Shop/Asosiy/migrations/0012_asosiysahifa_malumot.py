# Generated by Django 5.0 on 2023-12-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0011_delete_productdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='asosiysahifa',
            name='malumot',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]