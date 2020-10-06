from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('subjects/', views.subjects, name="subjects"),
    path('login/', views.login, name="login"),
    path('subjects/legal_aspects_of_business/',
         views.legal_aspects_of_business, name="legal_aspects_of_business"),
    path('subjects/legal_aspects_of_business/legal_aspects_questions/',
         views.legal_aspects_questions, name="legal_aspects_questions"),
    path('subjects/legal_aspects_of_business/legal_aspects_answers/',
         views.legal_aspects_answers, name="legal_aspects_answers"),
    path('subjects/corporate_accounting/',
         views.corporate_accounting, name="corporate_accounting"),
    path('subjects/corporate_accounting/corporate_accounting_questions/',
         views.corporate_accounting_questions, name="corporate_accounting_questions"),
    path('subjects/corporate_accounting/corporate_accounting_answers/',
         views.corporate_accounting_answers, name="corporate_accounting_answers"),
    path('subjects/personnel_management/',
         views.personnel_management, name="personnel_management"),
    path('subjects/personnel_management/personnel_management_questions/',
         views.personnel_management_questions, name="personnel_management_questions"),
    path('subjects/personnel_management/personnel_management_answers/',
         views.personnel_management_answers, name="personnel_management_answers"),

]
