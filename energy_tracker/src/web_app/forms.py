from django.forms import ModelForm, Textarea, TextInput
from django.utils.translation import gettext_lazy as _
from bootstrap_datepicker_plus.widgets import DatePickerInput

from .models import EnergyData


class EnergyDataForm(ModelForm):
    class Meta:
        model = EnergyData
        fields = "__all__"
        widgets = {
            "energy_buy": TextInput(
                attrs={"class": "form-control", "placeholder": "Zählerstand 180"}
            ),
            "energy_sell": TextInput(
                attrs={"class": "form-control", "placeholder": "Zählerstand 280"}
            ),
            "date_read": DatePickerInput(options={"format": "DD/MM/YYYY"}),
            "comment": Textarea(
                attrs={"class": "form-control", "placeholder": "Info wenn notwendig"}
            ),
        }
