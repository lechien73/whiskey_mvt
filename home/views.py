from django.shortcuts import render
from django.views import generic

from .models import Whiskey

# Create your views here.


class WhiskeyList(generic.ListView):
    model = Whiskey
    template_name = "home/index.html"
