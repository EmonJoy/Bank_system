from django.contrib import admin
from .models import BankAccount, Transaction

# ✅ BankAccount admin customization
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'account_number', 'balance')
    search_fields = ('account_number', 'user__username', 'user__email')
    list_filter = ('user',)
    ordering = ('-balance',)

admin.site.register(BankAccount, BankAccountAdmin)

# ✅ Transaction admin customization
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'amount', 'timestamp')
    search_fields = ('account__account_number', 'transaction_type')
    list_filter = ('transaction_type', 'timestamp')
    ordering = ('-timestamp',)

admin.site.register(Transaction, TransactionAdmin)
