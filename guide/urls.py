from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('guide/', views.guide, name="guide"),
    path('guide/upload_questions/', views.upload_question, name="upload_question"),
    path('guide/upload_answers/', views.upload_answer, name="upload_answer")
]
