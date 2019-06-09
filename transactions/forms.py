from django import forms
from .models import Transaction


class TransactionAddForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('file', 'amount', 'pages', 'payment_mode', 'color_model', 'copies', 'paper_type',
                  'details', 'station_class')
