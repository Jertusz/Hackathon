from django import forms


class queryForm(forms.Form):
<<<<<<< HEAD
    q = forms.CharField(label="", max_length=100, required=False)
    diet = forms.DecimalField(label="", max_value=5, required=False)
    calories = forms.DecimalField(label="", max_digits=4, required=False)
    max_products = forms.DecimalField(label="", max_digits=1, required=False)
=======
    q = forms.CharField(initial='', label="", max_length=100, widget=forms.HiddenInput())
    diet = forms.DecimalField(label="", max_value=5, initial=None, required=False)
    calories = forms.DecimalField(label="", max_digits=4, initial=None, required=False)
    max_products = forms.DecimalField(label="", max_digits=1, initial=None, required=False)
>>>>>>> a42b43c72ba78e7fe9fc25e04ec6f9bcd4c1c3c1
