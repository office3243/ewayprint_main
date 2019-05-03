from django.db import models
from wallets.models import Wallet
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class OfferPack(models.Model):
    name = models.CharField(max_length=16)
    headline = models.CharField(max_length=48)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CustomPack(models.Model):
    balance = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return str(self.balance)


class Recharge(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)

    pack_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    pack_id = models.PositiveIntegerField()
    pack = GenericForeignKey('pack_type', 'pack_id')

    created_on = models.DateTimeField(auto_now_add=True)

    payment_success = models.BooleanField(default=False)
    success = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.wallet, self.pack)


# def add_balance_to_wallet(sender, instance, *args, **kwargs):
