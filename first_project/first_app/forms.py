from django import forms
from django.core import validators

def check_for_z(value):
    print(value)
    if value[0].lower() != 'z':
        raise forms.ValidationError('Need to Start with z')

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea, label="Memo")
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail:
            raise forms.ValidationError('Email mismatch')
