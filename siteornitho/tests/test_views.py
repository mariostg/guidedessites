from django.test import TestCase, Client
from django.contrib import messages


class CatalogueTest(TestCase):
    def test_catalogue_has_no_sites(self):
        c = Client()
        response = c.get("/sites/catalogue/")
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Il n'y a pas de sites dans le catalogue", html=True)
