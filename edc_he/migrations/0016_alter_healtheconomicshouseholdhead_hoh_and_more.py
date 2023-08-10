# Generated by Django 4.2.3 on 2023-08-10 03:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_he", "0015_alter_healtheconomicsincome_external_remit_value_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healtheconomicshouseholdhead",
            name="hoh",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="If YES, STOP and save the form.",
                max_length=15,
                verbose_name="Are you the household head?",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicshouseholdhead",
            name="hoh_age",
            field=models.IntegerField(
                blank=True,
                help_text="In years as of today",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(18),
                    django.core.validators.MaxValueValidator(110),
                ],
                verbose_name="How old is the household head?",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicshouseholdhead",
            name="hoh_education_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="Highest level of education completed by the household head?",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicshouseholdhead",
            name="hoh_employment_type_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="Household head’s type of employment",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicshouseholdhead",
            name="hoh_ethnicity_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="What is the household head’s ethnic background?",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicshouseholdhead",
            name="hoh_gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=15,
                verbose_name="Is the household head female or male?",
            ),
        ),
        migrations.AlterField(
            model_name="healtheconomicshouseholdhead",
            name="hoh_religion_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="How would you describe the household head’s religious orientation?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicshouseholdhead",
            name="hoh",
            field=models.CharField(
                choices=[("Yes", "Yes"), ("No", "No")],
                help_text="If YES, STOP and save the form.",
                max_length=15,
                verbose_name="Are you the household head?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicshouseholdhead",
            name="hoh_age",
            field=models.IntegerField(
                blank=True,
                help_text="In years as of today",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(18),
                    django.core.validators.MaxValueValidator(110),
                ],
                verbose_name="How old is the household head?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicshouseholdhead",
            name="hoh_education_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="Highest level of education completed by the household head?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicshouseholdhead",
            name="hoh_employment_type_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="Household head’s type of employment",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicshouseholdhead",
            name="hoh_ethnicity_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="What is the household head’s ethnic background?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicshouseholdhead",
            name="hoh_gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female"), ("N/A", "Not applicable")],
                default="N/A",
                max_length=15,
                verbose_name="Is the household head female or male?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalhealtheconomicshouseholdhead",
            name="hoh_religion_old",
            field=models.CharField(
                editable=False,
                max_length=25,
                verbose_name="How would you describe the household head’s religious orientation?",
            ),
        ),
    ]
