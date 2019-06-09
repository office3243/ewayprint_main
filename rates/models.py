from django.db import models
from simple_history.models import HistoricalRecords


class Rate(models.Model):
    bw_rate = models.DecimalField(max_digits=4, decimal_places=2)
    color_rate = models.DecimalField(max_digits=4, decimal_places=2)

    history = HistoricalRecords()

    def __str__(self):
        return "bw : {} - color : {}".format(self.bw_rate, self.color_rate)
