from django.test import TestCase

from siteornitho.forms import SiteForm


class SiteFormTest(TestCase):
    def test_latitude_exceed_90(self):
        data = {"url": "www.mysite.com", "latitude": 190}
        form = SiteForm(data=data)
        self.assertEqual(form.errors["latitude"], ["Latitude ne peux excéder 90"])

    def test_latitude_less_than_minus_90(self):
        data = {"url": "www.mysite.com", "latitude": -110}
        form = SiteForm(data=data)
        self.assertEqual(form.errors["latitude"], ["Latitude ne peux être inférieure à -90"])

    def test_longitude_less_than_minus_180(self):
        data = {"url": "www.mysite.com", "longitude": -220}
        form = SiteForm(data=data)
        self.assertEqual(
            form.errors["longitude"], ["Longitude ne peux être inférieure à -180"], f"Longitude is {data['longitude']}"
        )

    def test_longitude_exceed_180(self):
        data = {"url": "www.mysite.com", "longitude": 220}
        form = SiteForm(data=data)
        self.assertEqual(form.errors["longitude"], ["Longitude ne peux excéder 180"])

    def test_locid_does_not_begin_with_letter(self):
        data = {"locid": "-1234567"}
        form = SiteForm(data=data)
        self.assertEqual(form.errors["locid"], ["Localisation doit débuter avec une lettre"])
