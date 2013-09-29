from django import forms

class ActivationForm(forms.Form):
    roll_no = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Roll No','name':'roll_no'}))

    fb_profile = forms.EmailField(required=True,
         widget=forms.TextInput(attrs={'class':'form-control',
            'placeholder':'Facebook Link', 'name':'fb_profile'}))