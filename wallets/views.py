from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from recharges.models import OfferPack


class WalletView(LoginRequiredMixin, TemplateView):
    template_name = 'wallet/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wallet'] = self.request.user.wallet
        context['offer_packs'] = OfferPack.objects.get_offer_packs()
        return context
