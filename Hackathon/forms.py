from django import forms

class queryForm(forms.Form):
    q = forms.CharField(label="", max_length=100)
    diet = forms.DecimalField(label="", max_value=5)
    calories = forms.DecimalField(label="", max_digits=4)
    max_products = forms.DecimalField(label="", max_digits=1)