# Generated by Django 4.2.1 on 2023-05-23 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("edc_he", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricalReligions",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "plural_name",
                    models.CharField(max_length=250, null=True, verbose_name="Plural name"),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                ("version", models.CharField(default="1.0", editable=False, max_length=35)),
                ("id", models.IntegerField(blank=True, db_index=True)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Religions",
                "verbose_name_plural": "historical Religions",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalNationalities",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "plural_name",
                    models.CharField(max_length=250, null=True, verbose_name="Plural name"),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                ("version", models.CharField(default="1.0", editable=False, max_length=35)),
                ("id", models.IntegerField(blank=True, db_index=True)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Nationalities",
                "verbose_name_plural": "historical Nationalities",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalInsuranceTypes",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "plural_name",
                    models.CharField(max_length=250, null=True, verbose_name="Plural name"),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                ("version", models.CharField(default="1.0", editable=False, max_length=35)),
                ("id", models.IntegerField(blank=True, db_index=True)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Insurance Types",
                "verbose_name_plural": "historical Insurance Types",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalEthnicities",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "plural_name",
                    models.CharField(max_length=250, null=True, verbose_name="Plural name"),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                ("version", models.CharField(default="1.0", editable=False, max_length=35)),
                ("id", models.IntegerField(blank=True, db_index=True)),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Ethnicities",
                "verbose_name_plural": "historical Ethnicities",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]