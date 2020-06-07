from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    char = list('abcdefghijklmnoprstuvwxyz')

    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        char.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        char.extend(list('0123456789'))

    length = int(request.GET.get('length',12))

    password = ''
    for i in range(length):
        password += random.choice(char)

    return render(request, 'generator/password.html', {
        'password': password
    })

def about(request):
    return render(request, 'generator/about.html')
