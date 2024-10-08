# Generated by Django 4.2.15 on 2024-08-21 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companyApp", "0003_service"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_image", models.CharField(blank=True, max_length=225, null=True)),
                ("rating", models.IntegerField()),
                ("username", models.CharField(max_length=200)),
                ("user_job_title", models.CharField(max_length=100)),
                ("review", models.TextField()),
            ],
        ),
    ]
