from django.shortcuts import render, redirect, get_object_or_404
from .models import Recharge, OfferPack, CustomPack
# from payments.models import
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import alert_messages


@login_required
def create_with_offer_pack(request, offer_pack_id):
    offer_pack = get_object_or_404(OfferPack, id=offer_pack_id, active=True)
    wallet = request.user.get_wallet
    recharge = Recharge.objects.create(wallet=wallet, pack=offer_pack)
    messages.success(request, alert_messages.RECHARGE_CREATED_MESSAGE)
    return redirect('portal:home')


@login_required
def create_with_custom_pack(request):
    if request.method == "POST":
        custom_price = request.POST['custom_price']
        custom_pack = CustomPack.objects.create(price=custom_price, balance=custom_price)
        wallet = request.user.get_wallet
        recharge = Recharge.objects.create(wallet=wallet, pack=custom_pack)
        messages.success(request, alert_messages.RECHARGE_CREATED_MESSAGE)
        return redirect('portal:home')
    else:
        return redirect("wallets:view")