from django import forms


class queryForm(forms.Form):
    q = forms.CharField(label="", max_length=100, required=False)
    diet = forms.DecimalField(label="", max_value=5, required=False)
    calories = forms.DecimalField(label="", max_digits=4, required=False)
    max_products = forms.DecimalField(label="", max_digits=1, required=False)
