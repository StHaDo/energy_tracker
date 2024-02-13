from typing import Any

from django.db import models
from datetime import datetime


# Create your models here.
class EnergyData(models.Model):
    energy_buy = models.IntegerField("Einkauf")
    energy_sell = models.IntegerField("Einspeisung")
    comment = models.TextField(blank=True, null=True)
    date_read = models.DateField("Ablesedatum", default=datetime.now)
    last_change = models.DateField("Letze Änderung", auto_now=True)

    data = models.Manager()

    def __str__(self) -> str:
        return f"Stand {self.date_read.strftime('%B')}"
