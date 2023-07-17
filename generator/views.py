from django.shortcuts import render
import random
# Create your views here.


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    generated_password = ''

    for x in range(10):
        generated_password += random.choice(characters)


    return render(request, 'password.html')
