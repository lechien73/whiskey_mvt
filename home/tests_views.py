from django.test import TestCase
from django.shortcuts import reverse
from .models import Whiskey, Distillery

# Create your tests here.


class TestViews(TestCase):

    def setUp(self):
        self.distillery = Distillery(name="Teelings")
        self.distillery.save()
        self.whiskey = Whiskey(name="Calvados cask",
                               distillery=self.distillery, rating=3, notes="Grand")
        self.whiskey.save()

    def test_get_whiskey_list(self):

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_get_edit_form(self):

        response = self.client.get(reverse("edit", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/edit.html")
        self.assertIn(b"Calvados", response.content)
