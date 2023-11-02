from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render (request, 'index.html')


def shop(request):
    return render (request, 'shop.html' )


def about(request):
    return render (request, 'about.html')


def services(request):
    return render (request, 'services.html')


def blog(request):
    return render (request, 'blog.html')


def contact(request):
    return render (request, 'contact.html')

