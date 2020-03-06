from django.shortcuts import render
from random import choice

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list("!@#$%^&*()"))

    length = int(request.GET.get('length', 13))

    thepassword = ''
    for i in range(length):
        thepassword = thepassword + choice(characters)
        if i==49:
            break

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/about.html')
