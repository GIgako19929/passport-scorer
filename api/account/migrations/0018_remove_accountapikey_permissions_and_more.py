# Generated by Django 4.2 on 2023-05-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0017_rename_allo_scorer_id_community_external_scorer_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="accountapikey",
            name="permissions",
        ),
        migrations.AddField(
            model_name="accountapikey",
            name="create_scorers",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="accountapikey",
            name="read_scores",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="accountapikey",
            name="submit_passports",
            field=models.BooleanField(default=True),
        ),
    ]