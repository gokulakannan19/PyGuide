from django.contrib import admin
from .models import Account, Question, Answer

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')


admin.site.register(Account, AccountAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 's_no')


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 's_no')


admin.site.register(Answer, AnswerAdmin)
