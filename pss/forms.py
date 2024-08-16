# forms.py
from typing import Any
from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'name', 'membership_type', 'address', 'date_of_birth',
            'phone_number', 'email', 'year_at_panyango', 'occupation', 'membership_fee', 'image'
        ]

    def clean(self):
        cleaned_data = super().clean()
        membership_type = cleaned_data.get('membership_type')
        membership_fee = cleaned_data.get('membership_fee')

        membership_fees = {
            'Ordinary': 5000,
            'Premium': 10000,
            'Vip': 15000,
            'Gold': 20000
        }

        if membership_type in membership_fees:
            required_fee = membership_fees[membership_type]
            if membership_fee < required_fee:
                self.add_error('membership_fee', f'The fee for {membership_type} membership should be at least {required_fee}.')

        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True

     
from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'email', 'amount']

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        print(f"Validating amount: {amount}")  # Debug print
        if amount < 5500:
            print("Validation failed: Amount is less than 5500")  # Debug print
            raise forms.ValidationError('The subscription amount must be at least 5500.')
        return amount

