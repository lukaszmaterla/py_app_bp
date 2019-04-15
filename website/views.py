from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = 'hello there...'
    return render(request, 'hello_word.html', {"title": my_title})


def about(request):
    return render(request, 'about.html', {"title": "About us"})


def contact(request):
    return render(request, 'hello_word.html', {"title": "Contact us"})