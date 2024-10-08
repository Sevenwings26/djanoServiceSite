# Generated by Django 4.2.15 on 2024-08-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GenerateInfo",
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
                (
                    "company_name",
                    models.CharField(default="Company Name", max_length=222),
                ),
                ("location", models.CharField(max_length=300)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("open_hours", models.CharField(blank=True, max_length=100, null=True)),
                ("video_url", models.URLField(blank=True, null=True)),
                ("twitter_url", models.URLField(blank=True, null=True)),
                ("facebook_url", models.URLField(blank=True, null=True)),
                ("instagram_url", models.URLField(blank=True, null=True)),
                ("linkedin_url", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
