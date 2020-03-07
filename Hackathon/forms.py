from django import forms


class queryForm(forms.Form):

    q = forms.CharField(initial='', label="", max_length=100, widget=forms.HiddenInput())
    diet = forms.DecimalField(label="", max_value=5, initial=None, required=False)
    calories = forms.DecimalField(label="", max_digits=4, initial=None, required=False)
    max_products = forms.DecimalField(label="", max_digits=1, initial=None, required=False)

