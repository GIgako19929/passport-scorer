# Generated by Django 4.2.6 on 2024-07-04 12:46

import account.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("passport_admin", "0005_alter_passportbanner_application"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
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
                ("notification_id", models.CharField(max_length=255, unique=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("custom", "Custom"),
                            ("stamp_expiry", "Stamp Expiry"),
                            ("on_chain_expiry", "OnChain Expiry"),
                            ("deduplication", "Deduplication"),
                        ],
                        db_index=True,
                        default="custom",
                        max_length=50,
                    ),
                ),
                ("is_active", models.BooleanField(default=False)),
                ("link", models.CharField(blank=True, max_length=255, null=True)),
                ("link_text", models.CharField(blank=True, max_length=255, null=True)),
                ("content", models.TextField()),
                ("created_at", models.DateField(auto_now_add=True)),
                ("expires_at", models.DateField(blank=True, null=True)),
                (
                    "eth_address",
                    account.models.EthAddressField(
                        blank=True, max_length=42, null=True
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="dismissedbanners",
            name="address",
            field=account.models.EthAddressField(max_length=42),
        ),
        migrations.CreateModel(
            name="NotificationStatus",
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
                ("is_read", models.BooleanField(default=False)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "eth_address",
                    account.models.EthAddressField(db_index=True, max_length=42),
                ),
                (
                    "notification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="passport_admin.notification",
                    ),
                ),
            ],
        ),
    ]
