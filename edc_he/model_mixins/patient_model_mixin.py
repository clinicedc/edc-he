from django.db import models
from edc_constants.choices import YES_NO

from ..choices import (
    EDUCATION_CHOICES,
    EMPLOYEMENT_CHOICES,
    EMPLOYEMENT_STATUS_CHOICES,
    ETHNICITY_CHOICES,
    MARITAL_CHOICES,
    RELIGION_CHOICES,
)
from ..models import InsuranceTypes


class PatientModelMixin(models.Model):
    pat_citizen = models.CharField(
        verbose_name="Is the household head a Ugandan national?",
        max_length=15,
        choices=YES_NO,
    )

    pat_religion = models.CharField(
        verbose_name="How would you describe your religious orientation?",
        max_length=25,
        choices=RELIGION_CHOICES,
    )

    pat_ethnicity = models.CharField(
        verbose_name="What is your ethnic background?",
        max_length=25,
        choices=ETHNICITY_CHOICES,
    )

    pat_education = models.CharField(
        verbose_name="Highest level of education completed?",
        max_length=25,
        choices=EDUCATION_CHOICES,
    )

    pat_employment = models.CharField(
        verbose_name="What is your employment status?",
        max_length=25,
        choices=EMPLOYEMENT_STATUS_CHOICES,
    )

    pat_employment_type = models.CharField(
        verbose_name="What is your type of employment?",
        max_length=25,
        choices=EMPLOYEMENT_CHOICES,
    )

    pat_marital_status = models.CharField(
        verbose_name="What is your marital status?",
        max_length=25,
        choices=MARITAL_CHOICES,
    )

    pat_insurance = models.ManyToManyField(
        InsuranceTypes,
        verbose_name="What is your health insurance status?",
    )

    class Meta:
        abstract = True
