from django.contrib import admin
from .models import Account, LegalAspectsOfBusiness, CorporateAccounting, Answer

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')


admin.site.register(Account, AccountAdmin)


class LegalAspectsOfBusinessAdmin(admin.ModelAdmin):
    list_display = ('question', 's_no')


admin.site.register(LegalAspectsOfBusiness, LegalAspectsOfBusinessAdmin)


class CorporateAccountingAdmin(admin.ModelAdmin):
    list_display = ('question', 's_no')


admin.site.register(CorporateAccounting, CorporateAccountingAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 's_no')


admin.site.register(Answer, AnswerAdmin)
