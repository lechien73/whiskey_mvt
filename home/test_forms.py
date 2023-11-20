from django.test import TestCase
from .forms import EditForm

# Create your tests here.


class TestEditForm(TestCase):

    def test_form_is_valid(self):
        edit_form = EditForm(
            {"notes": "Very nice", "rating": 1})

        self.assertTrue(edit_form.is_valid(), msg="Form is not valid")

    def test_notes_is_required(self):
        edit_form = EditForm(
            {"notes": "", "rating": 1})

        self.assertFalse(edit_form.is_valid(), msg="Form is valid")
