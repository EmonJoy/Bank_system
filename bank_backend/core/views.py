from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import BankAccount
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirm_password')
        account_number = request.POST.get('account_number')  
        if not account_number:
            messages.error(request, "Account number is required.")
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'register.html')
        if BankAccount.objects.filter(account_number=account_number).exists():
            messages.error(request, "Account number already exists.")
            return render(request, 'register.html')

        if password != confirmPassword:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        
        user = User.objects.create_user(username=username, password=password)
        user.save()

        
        BankAccount.objects.create(
            user=user,
            account_number=account_number,
            balance=0.00
        )

        messages.success(request, "Registration successful!")
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


def Dashboard(request):
    return render(request,'dashboard.html',{})