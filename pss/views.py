from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')
def apply(request):
    return render(request, 'register.html')
def success(request):
    return render(request, 'success.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            registration = form.save()
            return render(request, 'success.html', {'registration': registration})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriptionForm

def subscription_view(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription successful! Thank you for your Monthly Subscription.')
            return redirect('subscription')
        else:
            print(form.errors)  # Debug print
            messages.error(request, 'Please correct the errors above.')
    else:
        form = SubscriptionForm()
    
    return render(request, 'subscription.html', {'form': form})
