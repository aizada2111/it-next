from django import forms
from .models import Contact

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['website_url', 'your_name', 'email_address', 'phone_number', 'message']
        widgets = {
            'website_url': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Website url'}),
            'your_name': forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Your name'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-group', 'placeholder': 'Email address'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-group', 'placeholder': 'Phone number'}),
            'message': forms.Textarea(attrs={'class': 'form-group', 'placeholder': 'Message'}),

        }