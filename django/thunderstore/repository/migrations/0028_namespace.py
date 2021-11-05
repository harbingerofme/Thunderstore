# Generated by Django 3.1.7 on 2021-12-03 10:50

import django.contrib.postgres.fields.citext
import django.db.models.deletion
from django.contrib.postgres.operations import CITextExtension
from django.db import migrations, models

import thunderstore.repository.validators


class Migration(migrations.Migration):

    dependencies = [
        ("repository", "0027_rename_uploader_identity_to_team"),
    ]

    operations = [
        CITextExtension(),
        migrations.CreateModel(
            name="Namespace",
            fields=[
                (
                    "name",
                    django.contrib.postgres.fields.citext.CICharField(
                        max_length=64,
                        primary_key=True,
                        serialize=False,
                        validators=[
                            thunderstore.repository.validators.PackageReferenceComponentValidator(
                                "Namespace name"
                            )
                        ],
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "team",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="namespaces",
                        to="repository.team",
                    ),
                ),
            ],
            options={
                "verbose_name": "namespace",
                "verbose_name_plural": "namespaces",
            },
        ),
    ]
