from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import EnergyData
from .forms import EnergyDataForm


# Create your views here.
def home(req):
    energy_data = EnergyData.data.all().order_by("-date_read")[:5]
    form = EnergyDataForm()

    context = {
        "title": "Zählerstand",
        "energy_data": energy_data,
        "form": form,
    }
    return render(req, "index.html", context)


def new_entry(req):
    if req.method == "POST":
        form = EnergyDataForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    return Http404("Keine Daten eingegeben!")
