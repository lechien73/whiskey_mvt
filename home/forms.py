from django import forms
from .models import Whiskey


class EditForm(forms.ModelForm):
    """
    Form class for users to edit a review and rating 
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Whiskey
        fields = ('notes','rating',)