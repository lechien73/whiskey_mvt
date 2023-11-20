from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic

from .forms import EditForm
from .models import Whiskey

# Create your views here.


class WhiskeyList(generic.ListView):
    model = Whiskey
    template_name = "home/index.html"


def EditWhiskey(request, id):

    queryset = Whiskey.objects.all()
    whiskey = get_object_or_404(queryset, id=id)

    if request.method == "POST":
        edit_form = EditForm(data=request.POST, instance=whiskey)
        edit_form.save()
        return HttpResponseRedirect(reverse('home'))

    edit_form = EditForm({"notes": whiskey.notes, "rating": whiskey.rating})
    return render(request, "home/edit.html", {"whiskey": whiskey, "edit_form": edit_form})
