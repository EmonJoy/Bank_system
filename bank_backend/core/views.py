from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import BankAccount, Transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from decimal import Decimal 
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



@login_required(login_url='login')
def Dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard.html', {'user': request.user})


def index(request):

    return render(request,'index.html')

@login_required
def transaction_list(request):
    user = request.user

    if not hasattr(user, 'bankaccount'):
        messages.error(request, "No account found.")
        return redirect('index')
    
    account = user.bankaccount

    if request.method == "POST":
        trans_type = request.POST.get('type')
        amount = request.POST.get('amount')
        details = request.POST.get('description')

        try:
            amount = Decimal(amount)

            if amount <= 0:
                messages.error(request, "Amount must be positive.")
                return redirect('transaction')

            if trans_type == 'deposit':
                Transaction.objects.create(
                    account=account,
                    transaction_type='DEPOSIT',
                    amount=amount,
                    details=details
                )
                account.balance += amount
                account.save()
                messages.success(request, "Deposit successful.")
                return redirect('dashboard')

            elif trans_type == 'withdrawal':
                if amount > account.balance:
                    messages.error(request, "Insufficient balance.")
                    return redirect('transaction')

                Transaction.objects.create(
                    account=account,
                    transaction_type='WITHDRAW',
                    amount=amount,
                    details=details
                )
                account.balance -= amount
                account.save()
                messages.success(request, "Withdrawal successful.")

            else:
                messages.error(request, "Invalid transaction type.")
                return redirect('transaction')

        except:
            messages.error(request, "Invalid input.")
            return redirect('transaction')

    transactions = Transaction.objects.filter(account=account).order_by('-timestamp')
    return render(request, 'transaction.html', {'transactions': transactions})


    