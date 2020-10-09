from django.contrib import admin
from .models import Account, LegalAspectsOfBusiness, CorporateAccounting, PersonnelManagement, IncomeTax, AdvertisementAndSalesmanhip, Answer

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


class PersonnelManagementAdmin(admin.ModelAdmin):
    list_display = ('question', 's_no')


admin.site.register(PersonnelManagement, PersonnelManagementAdmin)


class IncomeTaxAdmin(admin.ModelAdmin):
    list_display = ('question', 's_no')


admin.site.register(IncomeTax, IncomeTaxAdmin)


class AdvertisementAndSalesmanshipAdmin(admin.ModelAdmin):
    list_display = ('question', 's_no')


admin.site.register(AdvertisementAndSalesmanhip,
                    AdvertisementAndSalesmanshipAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 's_no')


admin.site.register(Answer, AnswerAdmin)
