# Generated by Django 4.2.6 on 2024-08-01 23:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ceramic_cache", "0022_ceramiccache_proof_value_revocation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ceramiccache",
            name="proof_value",
            field=models.CharField(db_index=True, max_length=256),
        ),
    ]