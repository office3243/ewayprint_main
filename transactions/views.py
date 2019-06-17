from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TransactionAddForm
from django.urls import reverse_lazy
import random
from .models import Transaction
from django.views.generic import TemplateView, ListView
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib import messages
from django.conf import settings
from . import alert_messages
from stations.models import Station
from django.utils import timezone
from stations.models import Station, StationClass
import json


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rates_dict = StationClass.objects.first().rate.get_rates_dict
        context['rates_dict'] = json.dumps(rates_dict)
        return context

    def form_valid(self, form):

        if form.instance.payment_mode == "AC":
            if form.instance.amount > self.request.user.wallet.balance:
                messages.warning(self.request, settings.INSUFFICIENT_BALANCE_MESSAGE)
                return redirect("wallets:view")
            else:
                self.request.user.wallet.deduct_amount(form.instance.amount)
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
    context_object_name = 'transactions'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset().filter(user=self.request.user, is_hidden=False)
        return qs


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = "transactions/detail.html"
    context_object_name = "transaction"
    slug_url_kwarg = "uuid"
    slug_field = "uuid"

    def get_object(self, queryset=None):
        transaction = super().get_object()
        if transaction.user == self.request.user:
            return transaction
        else:
            raise Http404("No Transaction Found")

#
# class TransactionDeleteView(LoginRequiredMixin, View):
#
#     def get(self):
#         return redirect("portal:home")


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "transactions/delete.html"
    model = Transaction
    success_url = reverse_lazy('transactions:list')
    context_object_name = "transaction"
    slug_url_kwarg = "uuid"
    slug_field = "uuid"

    def get_object(self, queryset=None):
        transaction = super().get_object()
        if transaction.user == self.request.user and not transaction.is_printed:
            return transaction
        else:
            raise Http404("No Transaction Found")

    def delete(self, request, *args, **kwargs):
        transaction = self.get_object()
        if transaction.payment_mode == "AC":
            message = alert_messages.TRANSACTION_DELETED_WITH_REFUND_MESSGAE.format(transaction.amount)
            transaction.user.wallet.balance += transaction.amount
            transaction.user.wallet.save()
            messages.success(self.request, message)
        else:
            messages.success(self.request, alert_messages.TRANSACTION_DELETED_MESSGAE)
        return super().delete(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     messages.success(self.request, alert_messages.TRANSACTION_DELETED_MESSGAE)
    #     return super().delete(request, *args, **kwargs)
    #


class TransactionHideView(LoginRequiredMixin, DeleteView):
    template_name = "transactions/hide.html"
    model = Transaction
    success_url = reverse_lazy('transactions:list')
    context_object_name = "transaction"
    slug_url_kwarg = "uuid"
    slug_field = "uuid"

    def get_object(self, queryset=None):
        transaction = super().get_object()
        if transaction.user == self.request.user and transaction.is_printed and not transaction.is_hidden:
            return transaction
        else:
            raise Http404("No Transaction Found")

    def delete(self, request, *args, **kwargs):
        transaction = self.get_object()
        transaction.is_hidden = True
        transaction.save()
        messages.success(self.request, alert_messages.TRANSACTION_HIDEED_MESSGAE)
        return redirect(self.success_url)


def get_print(request, otp_1, otp_2, station_code):
    station = get_object_or_404(Station, station_code=station_code)
    transaction = Transaction.objects.get(otp_1=otp_1, otp_2=otp_2)
    try:
        file_printed = transaction.printed
        python_dict = {'otp_found': True, 'file_printed': file_printed, 'color_model': transaction.color_model,
                       'amount': transaction.amount, 'payment_mode': transaction.payment_mode, 'file_path': transaction.file.url}
        transaction.file_printed = True
        transaction.printed_station = station
        transaction.printed_on = timezone.now()
        transaction.save()
        return JsonResponse(python_dict, safe=False)
    except transaction.DoesNotExist:
        return JsonResponse({'otp_found': False})


