from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='First name', required=True)
    last_name = forms.CharField(max_length=100, label='Last name', required=True)
    email = forms.EmailField(label='E-mail', required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
