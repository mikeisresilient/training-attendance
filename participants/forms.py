from django import forms
from .models import Participant


class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = [
            "full_name",
            "designation",
            "department",
            "phone_number",
            "email",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your full name"
            }),
            "designation": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your designation"
            }),
            "department": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your department"
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your phone number"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email address"
            }),
        }