from faker import Faker
from model_bakery.recipe import Recipe

from edc_he.models import HealthEconomicsAssets, HealthEconomicsProperty

fake = Faker()

healtheconomicsassets = Recipe(HealthEconomicsAssets, subject_visit=None)
healtheconomicsproperty = Recipe(HealthEconomicsProperty, subject_visit=None)
