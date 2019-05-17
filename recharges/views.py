from recharges import alert_messages
from recharges.models import Recharge, OfferPack, CustomPack
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


import decimal


@login_required
def create_with_custom_pack(request):
    if request.method == "POST":
        custom_price = request.POST['custom_price']
        print(decimal.Decimal(custom_price))
        custom_pack = CustomPack.objects.create(price=decimal.Decimal(custom_price), balance=decimal.Decimal(custom_price))
        wallet = request.user.get_wallet
        recharge = Recharge.objects.create(wallet=wallet, pack=custom_pack)
        messages.success(request, alert_messages.RECHARGE_CREATED_MESSAGE)
        return redirect('portal:home')
    else:
        return redirect("wallets:view")


@login_required
def recharge_succeed(request, payment):
    messages.success(request, alert_messages.RECHARGE_SUCCEED_MESSAGE)
    return redirect("wallets:view")


@login_required
def recharge_failed(request, payment):
    messages.warning(request, alert_messages.RECHARGE_FAILED_MESSAGE)
    return redirect("wallets:view")

try:
    from payments.views import create_payment as p_create_payment
except:
    pass


@login_required
def create_with_offer_pack(request, offer_pack_id):
    offer_pack = get_object_or_404(OfferPack, id=offer_pack_id, active=True)
    recharge = Recharge.objects.create(user=request.user, pack=offer_pack)
    return p_create_payment(request, recharge)
    # messages.success(request, alert_messages.RECHARGE_CREATED_MESSAGE)
    # return redirect('portal:home')
