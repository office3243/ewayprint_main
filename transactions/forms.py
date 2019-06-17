from django import forms
from .models import Transaction


class TransactionAddForm(forms.ModelForm):

    payment_mode = forms.ChoiceField(choices=Transaction.PAYMENT_MODE_CHOICES, widget=forms.RadioSelect(attrs={'class': "custom-control custom-radio custom-control-input", 'id': "defaultGroupExample"}))
    color_model = forms.ChoiceField(choices=Transaction.COLOR_MODEL_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Transaction
        fields = ('file', 'pages', 'payment_mode', 'color_model', 'copies', 'refrence')

