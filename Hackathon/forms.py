from django import forms

class queryForm(forms.Form):
    q = forms.CharField(label="query", max_length=100)