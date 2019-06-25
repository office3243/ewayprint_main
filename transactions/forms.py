from django import forms
from .models import Transaction, File


class TransactionAddForm(forms.ModelForm):

    payment_mode = forms.ChoiceField(choices=Transaction.PAYMENT_MODE_CHOICES, widget=forms.RadioSelect(attrs={'class': "custom-control custom-radio custom-control-input", 'id': "defaultGroupExample"}))
    color_model = forms.ChoiceField(choices=Transaction.COLOR_MODEL_CHOICES, widget=forms.RadioSelect)

    # file_uuid = forms.CharField()
    pages = forms.IntegerField(widget=forms.NumberInput())

    class Meta:
        model = Transaction
        fields = ('pages', 'payment_mode', 'color_model', 'copies', 'reference')


class FileAddForm(forms.ModelForm):

    input_file = forms.FileField(widget=forms.FileInput(attrs={"required": "true"}))

    class Meta:
        model = File
        fields = ("input_file", )

