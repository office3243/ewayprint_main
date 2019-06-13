from django import forms
from .models import Transaction


class TransactionAddForm(forms.ModelForm):

    amount = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "ffor test class"}))

    class Meta:
        model = Transaction
        fields = ('file', 'amount', 'pages', 'payment_mode', 'color_model', 'copies', 'paper_type',
                  'refrence')
