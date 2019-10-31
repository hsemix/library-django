from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=254, widget=forms.PasswordInput)