from django import forms


class CreateAccountForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
