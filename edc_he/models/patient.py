from django.conf import settings
from django.db import models
from edc_crf.model_mixins import CrfModelMixin, SingletonCrfModelMixin
from edc_model.models import BaseUuidModel

from ..model_mixins import PatientModelMixin


class HealthEconomicsPatient(
    SingletonCrfModelMixin,
    PatientModelMixin,
    CrfModelMixin,
    BaseUuidModel,
):
    subject_visit = models.OneToOneField(
        settings.SUBJECT_VISIT_MODEL,
        on_delete=models.PROTECT,
        related_name="he_patient_subjectvisit",
    )

    class Meta(CrfModelMixin.Meta, BaseUuidModel.Meta):
        verbose_name = "Health Economics: Patient"
        verbose_name_plural = "Health Economics: Patient"
