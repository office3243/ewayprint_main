from __future__ import unicode_literals
from django.db import models
from django.conf import settings
import datetime
from django.db.models.signals import post_save, pre_delete, post_delete
import uuid
from django.urls import reverse_lazy
from .managers import TransactionManager
from django.contrib import messages
from . import alert_messages
from django.core.validators import FileExtensionValidator


USER_MODEL = settings.AUTH_USER_MODEL


class Transaction(models.Model):

    PAYMENT_MODE_CHOICES = (('AC', "Account"), ('CO', "Coin"))
    COLOR_MODEL_CHOICES = (('BW', 'Black&White'), ('CL', 'Colorful'))
    ALLOWED_FILE_TYPES = ("png", "jpg", "jpeg", "pdf")

    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    otp_1 = models.CharField(max_length=4)
    otp_2 = models.CharField(max_length=4)

    file = models.FileField(upload_to="transactions/transaction_files/{}/".format(datetime.date.today()),
                            validators=[FileExtensionValidator(allowed_extensions=ALLOWED_FILE_TYPES), ]
                            )

    payment_mode = models.CharField(max_length=2, choices=PAYMENT_MODE_CHOICES)
    color_model = models.CharField(max_length=2, default='BW', choices=COLOR_MODEL_CHOICES)
    copies = models.PositiveSmallIntegerField(default=1)
    station_class = models.ForeignKey('stations.StationClass', on_delete=models.CASCADE, default=1)

    amount = models.DecimalField(decimal_places=2, max_digits=5)
    pages = models.PositiveSmallIntegerField()

    created_on = models.DateTimeField(auto_now_add=True)

    is_printed = models.BooleanField(default=False)
    printed_on = models.DateTimeField(blank=True, null=True)
    is_hidden = models.BooleanField(default=False)

    printed_station = models.ForeignKey('stations.Station', on_delete=models.PROTECT, blank=True, null=True)

    is_permitted = models.BooleanField(default=True)

    refrence = models.CharField(max_length=64, blank=True)

    objects = TransactionManager

    def __str__(self):
        return str(self.user)

    @property
    def get_absolute_url(self):
        return reverse_lazy("transactions:detail", kwargs={"uuid": self.uuid})

    @property
    def get_delete_url(self):
        return reverse_lazy("transactions:delete", kwargs={"uuid": self.uuid})

    @property
    def get_hide_url(self):
        return reverse_lazy("transactions:hide", kwargs={"uuid": self.uuid})

    @property
    def get_display_text(self):
        if self.refrence:
            return self.refrence
        else:
            return self.file.name[-30:]


def assign_amount(sender, instance, *args, **kwargs):
    if instance.color_model == "BW":
        amount = instance.pages * instance.station_class.rate.bw_rate
    else:
        amount = instance.pages * instance.station_class.rate.color_rate
    if instance.amount != amount:
        instance.amount = amount
        instance.save()

#
# def refund_amount(sender, instance, *args, **kwargs):
#     if instance.is_permitted and not instance.is_printed and instance.payment_mode == "AC":
#         instance.user.wallet.balance += instance.amount
#         instance.user.wallet.save()
#         instance.is_permitted = False
#         instance.save()
#         instance.delete()
#
#
# pre_delete.connect(refund_amount, sender=Transaction)


post_save.connect(assign_amount, sender=Transaction)

#
# class File(models.Model):
#
#     FILE_TYPE_CHOICES = (('JPG', 'JPG'), ('PNG', 'PNG'), ('PDF', 'PDF'), ('TXT', 'TXT'))
#
#     input_file = models.FileField(upload_to="transactions/files/input_files/")
#     converted_file = models.FileField(upload_to="transactions/files/converted_files/", blank=True, null=True)
#
#     file_type = models.CharField(max_length="3", choices=FILE_TYPE_CHOICES, blank=True)
#
#     @property
#     def get_file_ext(self):
#         return self.input_file.name[(self.input_file.name.rfind(".")+1):]
#
#
#
# def convert_file(instance, sender, *args, **kwargs):
#     if not instance.input_file:
#
#
#
# def assign_file_type(sender, instance, *args, **kwargs):
#     file_type = instance.get_file_ext
#     if instance.file_type != file_type:
#         instance.file_type = file_type
#         instance.save()
