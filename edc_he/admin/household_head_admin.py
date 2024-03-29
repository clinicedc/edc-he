from django.contrib import admin
from django.db.models import Q
from edc_crf.modeladmin_mixins import CrfModelAdmin

from ..admin_site import edc_he_admin
from ..forms import HealthEconomicsHouseholdHeadForm
from ..modeladmin_mixins import HealthEconomicsHouseholdHeadModelAdminMixin
from ..models import Ethnicities, HealthEconomicsHouseholdHead, Religions


@admin.register(HealthEconomicsHouseholdHead, site=edc_he_admin)
class HealthEconomicsHouseholdHeadAdmin(
    HealthEconomicsHouseholdHeadModelAdminMixin, CrfModelAdmin
):
    form = HealthEconomicsHouseholdHeadForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if getattr(request, "site", None):
            if db_field.name == "hoh_ethnicity":
                kwargs["queryset"] = Ethnicities.objects.filter(
                    Q(extra_value=request.site.siteprofile.country)
                    | Q(extra_value__isnull=True)
                )
            if db_field.name == "hoh_religion":
                kwargs["queryset"] = Religions.objects.filter(
                    Q(extra_value=request.site.siteprofile.country)
                    | Q(extra_value__isnull=True)
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if getattr(request, "site", None):
            if db_field.name == "hoh_insurance":
                model_cls = getattr(self.model, db_field.name).field.related_model
                kwargs["queryset"] = model_cls.objects.filter(
                    Q(extra_value=request.site.siteprofile.country)
                    | Q(extra_value__isnull=True)
                )
        return super().formfield_for_manytomany(db_field, request, **kwargs)
