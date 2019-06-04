from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TransactionAddForm
from django.urls import reverse_lazy
import random
from .models import Transaction
from django.views.generic import TemplateView, ListView
from django.http import Http404, HttpResponse
from django.contrib import messages
from django.conf import settings


def generate_four_digit_otp():
    return ''.join(random.sample("0123456789", 4)), ''.join(random.sample("0123456789", 4))


def check_unique_otps():
    otp_1, otp_2 = generate_four_digit_otp()

    if Transaction.objects.filter(otp_1=otp_1, otp_2=otp_2).exists():
        return check_unique_otps()
    else:
        return otp_1, otp_2


class TransactionAddView(LoginRequiredMixin, CreateView):

    form_class = TransactionAddForm
    template_name = 'transactions/add.html'
    success_url = reverse_lazy('portal:home')

    def form_valid(self, form):

        if form.instance.payment_mode == "AC":
            if form.instance.amount > self.request.user.wallet.balance:
                messages.warning(self.request, settings.INSUFFICIENT_BALANCE_MESSAGE)
                return redirect("wallets:view")
            else:
                self.request.user.deduct_amount(form.instance.amount)

        otp_1, otp_2 = check_unique_otps()
        form.instance.otp_1 = otp_1
        form.instance.otp_2 = otp_2
        form.instance.user = self.request.user
        form.save()
        return redirect('transactions:get_otp', otp_1=otp_1, otp_2=otp_2)

    # def form_invalid(self, form):


class GetOtpView(LoginRequiredMixin, TemplateView):
    template_name = 'transactions/get_otp.html'


class TransactionListView(LoginRequiredMixin, ListView):

    model = Transaction
    template_name = 'transactions/list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset().filter(user=self.request.user)
        return qs

    def get_context_object_name(self, object_list):
        return "transactions"