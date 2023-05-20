from django.test import TestCase

from siteornitho.forms import SiteForm


class SiteFormTest(TestCase):
    def test_latitude_exceed_90(self):
        data = {"latitude": 190}
        form = SiteForm(data=data)
        self.assertEqual(form.errors["latitude"], ["Latitude ne peux excéder 90"])

    def test_latitude_less_than_90(self):
        data = {"latitude": -190}
        form = SiteForm(data=data)
        self.assertEqual(form.errors["latitude"], ["Latitude ne peux être inférieure à 90"])
