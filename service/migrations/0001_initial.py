# Generated by Django 5.1.4 on 2025-04-10 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceRequest",
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
                    "service_type",
                    models.CharField(
                        choices=[("free", "Free"), ("paid", "Paid")], max_length=10
                    ),
                ),
                ("service_description", models.TextField()),
                ("requested_date", models.DateField()),
                ("requested_time", models.TimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="service_requests",
                        to="customer.customer",
                    ),
                ),
            ],
            options={
                "db_table": "service_request",
            },
        ),
    ]
