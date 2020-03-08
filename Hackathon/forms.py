from django import forms


class queryForm(forms.Form):
    q = forms.CharField(initial='', label="", max_length=100,
                        widget=forms.HiddenInput())
