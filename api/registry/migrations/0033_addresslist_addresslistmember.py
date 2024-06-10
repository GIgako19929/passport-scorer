# Generated by Django 4.2.6 on 2024-06-10 22:21

import account.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("registry", "0032_delete_stake_delete_stakeevent"),
    ]

    operations = [
        migrations.CreateModel(
            name="AddressList",
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
                ("name", models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="AddressListMember",
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
                    "address",
                    account.models.EthAddressField(db_index=True, max_length=100),
                ),
                (
                    "list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to="registry.addresslist",
                    ),
                ),
            ],
            options={
                "unique_together": {("address", "list")},
            },
        ),
    ]
