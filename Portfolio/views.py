from django.shortcuts import render
from .models import Contact
import json
import requests

# Create your views here.


def home(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context = {'joker':joke}
        return render(request, 'Portfolio/home.html',context)
    else:
        firstname = 'Satyendra'
        lastname = 'Tiwari'
        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context = {'joker':joke}
        return render(request, 'Portfolio/home.html',context)


def portfolio(request):
    return render(request, 'Portfolio/portfolio.html')


def contact(request):
    if request.method == 'POST':
        name_r = request.POST.get('txtName')
        email_r = request.POST.get('txtEmail')
        phone_r = request.POST.get('txtPhone')
        msg_r = request.POST.get('txtMsg')
        c= Contact(name=name_r,email=email_r,phone=phone_r,subject=msg_r)
        c.save()
        return render(request, 'Portfolio/thankyou.html')
    else:
        return render(request, 'Portfolio/contact.html')
