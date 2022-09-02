from django import forms


class conForm(forms.Form):
    name = forms.CharField(max_length=10)
    mailid = forms.EmailField(max_length=50)
