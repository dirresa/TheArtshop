from django import forms
from artshop.models import Contact


class FormContact(forms.ModelForm):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control fh5co_contact_text_box',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control fh5co_contact_text_box',
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control fh5co_contact_text_box', 
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control fh5co_contacts_message', 
    }))

    class Meta:
        model = Contact
        # fields = ['name', 'email', 'subject', 'message']
        exclude = ['created']       # Khai bao tat ca tru 'created'
