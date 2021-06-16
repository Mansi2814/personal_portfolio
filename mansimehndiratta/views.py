from django.shortcuts import render
from mansimehndiratta.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):

    context = {
        'variable1': 'Hello'
    }
    return render(request, 'index.html', context)


def aboutus(request):
    return render(request, 'about.html')


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been received!.')
    return render(request, 'contact.html')


def projects(request):
    return render(request, 'projects.html')


def experiences(request):
    return render(request, 'experiences.html')


def internships(request):
    return render(request, 'internships.html')
