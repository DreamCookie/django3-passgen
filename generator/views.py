from django.shortcuts import render
from django.http import HttpResponse
import random as rand
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('Uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()-+_='))
    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))



    length = int(request.GET.get('length', 5))

    thepassword = ''
    for x in range(length):
        thepassword += rand.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword} )

def help(request):
    return render(request, 'generator/help.html')
