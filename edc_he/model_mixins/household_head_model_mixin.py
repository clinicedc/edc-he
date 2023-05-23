from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from edc_constants.choices import GENDER, YES_NO

from ..choices import (
    EDUCATION_CHOICES,
    EMPLOYEMENT_CHOICES,
    EMPLOYEMENT_STATUS_CHOICES,
    ETHNICITY_CHOICES,
    MARITAL_CHOICES,
    RELATIONSHIP_CHOICES,
    RELIGION_CHOICES,
)
from ..models import InsuranceTypes


class HouseholdHeadModelMixin(models.Model):
    # head of household
    hoh = models.CharField(
        verbose_name="Are you the household head?",
        max_length=15,
        choices=YES_NO,
        help_text=(
            "Note: By head of the household we mean the main decision maker "
            "in the household. The head can be either male or female. If two "
            "people are equal decision-makers, take the older person. [Q1]"
        ),
    )

    relationship_to_hoh = models.CharField(
        verbose_name="What is your relationship to the household head?",
        max_length=25,
        choices=RELATIONSHIP_CHOICES,
        help_text="[Q1A]",
    )

    hoh_gender = models.CharField(
        verbose_name="Is the household head female or male?",
        max_length=15,
        choices=GENDER,
        help_text="[Q1B]",
    )

    hoh_age = models.IntegerField(
        verbose_name="How old is the household head?",
        validators=[MinValueValidator(18), MaxValueValidator(110)],
        help_text="In years. [Q1C]",
    )

    hoh_citizen = models.CharField(
        verbose_name="Is the household head a Ugandan national?",
        max_length=15,
        choices=YES_NO,
    )

    hoh_religion = models.CharField(
        verbose_name="How would you describe the household head’s religious orientation?",
        max_length=25,
        choices=RELIGION_CHOICES,
    )

    hoh_ethnicity = models.CharField(
        verbose_name="What is the household head’s ethnic background?",
        max_length=25,
        choices=ETHNICITY_CHOICES,
    )

    hoh_education = models.CharField(
        verbose_name="Highest level of education completed by the household head?",
        max_length=25,
        choices=EDUCATION_CHOICES,
    )

    hoh_employment = models.CharField(
        verbose_name="Household head’s employment status",
        max_length=25,
        choices=EMPLOYEMENT_STATUS_CHOICES,
    )

    hoh_employment_type = models.CharField(
        verbose_name="Household head’s type of employment",
        max_length=25,
        choices=EMPLOYEMENT_CHOICES,
    )

    hoh_marital_status = models.CharField(
        verbose_name="Household head’s marital status",
        max_length=25,
        choices=MARITAL_CHOICES,
    )

    hoh_insurance = models.ManyToManyField(
        InsuranceTypes,
        verbose_name="Household head’s health insurance and ‘club’ status ",
    )

    class Meta:
        abstract = True
