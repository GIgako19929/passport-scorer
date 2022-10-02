# Generated by Django 4.1.1 on 2022-10-01 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("registry", "0002_rename_stamp_id_stamp_hash"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApuScorer",
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
                ("start_time", models.DateTimeField(blank=True, null=True)),
                ("end_time", models.DateTimeField(blank=True, null=True)),
                (
                    "accepted_providers",
                    models.JSONField(blank=True, default=list, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Score",
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
                    "passport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="registry.passport",
                    ),
                ),
                (
                    "scorer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="scorer_apu.apuscorer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Combo",
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
                ("count", models.IntegerField(db_index=True, default=0)),
                (
                    "scorer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="scorer_apu.apuscorer",
                    ),
                ),
            ],
        ),
    ]
