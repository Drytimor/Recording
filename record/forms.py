from django import forms
from .models import PaymentTariffChoices, StatusOpeningChoices


class FilterEventsForm(forms.Form):
    tariff = forms.ChoiceField(label='Фильтр', widget=forms.CheckboxSelectMultiple, choices=PaymentTariffChoices.choices)
    open = forms.ChoiceField(label='', widget=forms.CheckboxSelectMultiple, choices=StatusOpeningChoices.choices)


