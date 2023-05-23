from edc_list_data.model_mixins import ListModelMixin


class InsuranceTypes(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Insurance Types"
        verbose_name_plural = "Insurance Types"


class Nationalities(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Nationalities"
        verbose_name_plural = "Nationalities"


class Religions(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Religions"
        verbose_name_plural = "Religions"


class Ethnicities(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Ethnicities"
        verbose_name_plural = "Ethnicities"
