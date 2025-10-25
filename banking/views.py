from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.contrib import messages
from .forms import RegisterForm, KYCForm
from .models import KYC

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('kyc_upload')
        messages.error(request, "Registration failed. Please check your inputs.")
    else:
        form = RegisterForm()
    return render(request, 'banking/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('kyc_upload')
    else:
        form = AuthenticationForm()
    return render(request, 'banking/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'banking/logout.html')


@login_required
def kyc_upload(request):
    if request.method == 'POST':
        form = KYCForm(request.POST, request.FILES)
        if form.is_valid():
            kyc = form.save(commit=False)
            kyc.user = request.user
            kyc.submitted_at = now()
            kyc.save()
            messages.success(request, "KYC submitted successfully!")
            return render(request, 'banking/kyc_upload.html', {'form': form, 'success': True})
    else:
        form = KYCForm()
    return render(request, 'banking/kyc_upload.html', {'form': form})


def password_reset(request):
    form = PasswordResetForm()
    return render(request, 'banking/password_reset.html', {'form': form})


@login_required
def kyc_status(request):
    try:
        kyc = KYC.objects.get(user=request.user)
    except KYC.DoesNotExist:
        kyc = None
    return render(request, 'banking/kyc_status.html', {'kyc': kyc})

