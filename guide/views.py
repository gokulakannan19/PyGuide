from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, Guide

# Create your views here.


def home(request):
    if request.method == 'POST':
        email = request.POST['input-email']
        name = request.POST['input-name']
        purpose = request.POST['options']
        print(email)
        print(name)
        print(purpose)

        Account.objects.create(email=email, name=name, purpose=purpose)

    else:
        return render(request, 'guide/home.html', {})


def guide(request):
    return render(request, 'guide/guide.html', {})
