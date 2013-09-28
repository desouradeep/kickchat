from django import forms

class RegistrationForm(forms.Form):

    firstname = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class':'form-control',
            'placeholder':'First Name', 'name':'firstname'}))

    lastname = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Last Name', 'name':'lastname'}))

    username = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Username','name':'username'}))

    email = forms.EmailField(required=True,
         widget=forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Email', 'name':'email'}))

    password = forms.CharField(required=True,
         widget=forms.PasswordInput(attrs={'class':'form-control',
            'placeholder':'Password', 'name':'password'}))

    password2 = forms.CharField(required=True,
         widget=forms.PasswordInput(attrs={'class':'form-control',
            'placeholder':'Confirm Password', 'name':'password2'}))

class LoginForm(forms.Form):
    username = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Username','name':'username'}))
    password = forms.CharField(required=True,
         widget=forms.PasswordInput(attrs={'class':'form-control',
            'placeholder':'Password', 'name':'password'}))
