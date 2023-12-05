# Generated by Django 4.2.7 on 2023-12-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_he", "0005_rename_employment_employmenttype_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="education",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Education",
                "verbose_name_plural": "Education",
            },
        ),
        migrations.AlterModelOptions(
            name="employmenttype",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Employment type",
                "verbose_name_plural": "Employment types",
            },
        ),
        migrations.AlterModelOptions(
            name="ethnicities",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Ethnicities",
                "verbose_name_plural": "Ethnicities",
            },
        ),
        migrations.AlterModelOptions(
            name="insurancetypes",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Insurance Types",
                "verbose_name_plural": "Insurance Types",
            },
        ),
        migrations.AlterModelOptions(
            name="nationalities",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Nationalities",
                "verbose_name_plural": "Nationalities",
            },
        ),
        migrations.AlterModelOptions(
            name="religions",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Religions",
                "verbose_name_plural": "Religions",
            },
        ),
        migrations.RemoveIndex(
            model_name="education",
            name="edc_he_educ_id_52260a_idx",
        ),
        migrations.RemoveIndex(
            model_name="employmenttype",
            name="edc_he_empl_id_810a9e_idx",
        ),
        migrations.RemoveIndex(
            model_name="ethnicities",
            name="edc_he_ethn_id_c14a61_idx",
        ),
        migrations.RemoveIndex(
            model_name="insurancetypes",
            name="edc_he_insu_id_79fd66_idx",
        ),
        migrations.RemoveIndex(
            model_name="nationalities",
            name="edc_he_nati_id_9a6ed2_idx",
        ),
        migrations.RemoveIndex(
            model_name="religions",
            name="edc_he_reli_id_e5b168_idx",
        ),
        migrations.AlterField(
            model_name="education",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AlterField(
            model_name="employmenttype",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="employmenttype",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="employmenttype",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AlterField(
            model_name="ethnicities",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="ethnicities",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="ethnicities",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AlterField(
            model_name="historicaleducation",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="historicalemploymenttype",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="historicalethnicities",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="historicalinsurancetypes",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="historicalnationalities",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="historicalreligions",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="insurancetypes",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="insurancetypes",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="insurancetypes",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AlterField(
            model_name="nationalities",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="nationalities",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="nationalities",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AlterField(
            model_name="religions",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="religions",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="religions",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AddIndex(
            model_name="education",
            index=models.Index(fields=["name"], name="edc_he_educ_name_64c0c9_idx"),
        ),
        migrations.AddIndex(
            model_name="education",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_he_educ_display_66a8e9_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="employmenttype",
            index=models.Index(fields=["name"], name="edc_he_empl_name_b36be4_idx"),
        ),
        migrations.AddIndex(
            model_name="employmenttype",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_he_empl_display_94ff23_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="ethnicities",
            index=models.Index(fields=["name"], name="edc_he_ethn_name_e7e98d_idx"),
        ),
        migrations.AddIndex(
            model_name="ethnicities",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_he_ethn_display_872238_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="insurancetypes",
            index=models.Index(fields=["name"], name="edc_he_insu_name_f9caac_idx"),
        ),
        migrations.AddIndex(
            model_name="insurancetypes",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_he_insu_display_751194_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="nationalities",
            index=models.Index(fields=["name"], name="edc_he_nati_name_cba5f6_idx"),
        ),
        migrations.AddIndex(
            model_name="nationalities",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_he_nati_display_178bbe_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="religions",
            index=models.Index(fields=["name"], name="edc_he_reli_name_b2fcb4_idx"),
        ),
        migrations.AddIndex(
            model_name="religions",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_he_reli_display_11bcd9_idx",
            ),
        ),
    ]