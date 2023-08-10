# Generated by Django 4.2.3 on 2023-08-10 03:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_he", "0017_remove_healtheconomicspatient_pat_citizen_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healtheconomicspatient",
            name="pat_education_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="Highest level of education completed?",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicspatient",
            name="pat_employment_type_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="What is your type of employment?",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicspatient",
            name="pat_ethnicity_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="What is your ethnic background?",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicspatient",
            name="pat_religion_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="How would you describe your religious orientation?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicspatient",
            name="pat_education_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="Highest level of education completed?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicspatient",
            name="pat_employment_type_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="What is your type of employment?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicspatient",
            name="pat_ethnicity_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="What is your ethnic background?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicspatient",
            name="pat_religion_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="How would you describe your religious orientation?",
            ),
        ),
    ]
