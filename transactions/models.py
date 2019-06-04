from __future__ import unicode_literals
from django.db import models
from django.conf import settings
import datetime
from django.db.models.signals import post_save


PAYMENT_MODE_CHOICES = (('AC', "Account"), ('CO', "Coin"))
COLOR_MODEL_CHOICES = (('BW', 'Black&White'), ('CL', 'Colorful'))
PAPER_TYPE_CHOICES = (('NM', 'Normal'), ('LT', 'Letter'), ('PP', "Photo Paper"))


class Transaction(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    file = models.FileField(upload_to="transactions/transaction_files/{}/".format(datetime.date.today()))
    otp_1 = models.CharField(max_length=4)
    otp_2 = models.CharField(max_length=4)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    pages = models.PositiveSmallIntegerField()
    payment_mode = models.CharField(max_length=2, choices=PAYMENT_MODE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    color_model = models.CharField(max_length=2, default='BW', choices=COLOR_MODEL_CHOICES)
    copies = models.PositiveSmallIntegerField(default=1)
    paper_type = models.CharField(max_length=2, default='NM', choices=PAPER_TYPE_CHOICES)

    is_printed = models.BooleanField(default=False)
    printed_on = models.DateTimeField(blank=True, null=True)

    printed_station = models.ForeignKey('stations.Station', on_delete=models.PROTECT, blank=True, null=True)
    station_class = models.ForeignKey('stations.StationClass', on_delete=models.CASCADE)

    is_permitted = models.BooleanField(default=True)

    details = models.TextField(blank=True)

    def __str__(self):
        return str(self.user)


def assign_amount(sender, instance, *args, **kwargs):
    if instance.color_model == "BW":
        amount = instance.pages * instance.station_class.rate.bw_rate
    else:
        amount = instance.pages * instance.station_class.rate.color_rate
    if instance.amount != amount:
        instance.amount = amount
        instance.save()


post_save.connect(assign_amount, sender=Transaction)
