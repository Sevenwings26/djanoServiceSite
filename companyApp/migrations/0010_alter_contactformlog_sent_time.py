# Generated by Django 4.2.15 on 2024-08-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companyApp", "0009_contactformlog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactformlog",
            name="sent_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
