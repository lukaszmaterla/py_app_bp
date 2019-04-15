from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = 'hello there...'
    return render(request, 'home.html', {"title": my_title})


def about(request):
    return render(request, 'about.html', {"title": "About us"})


def contact(request):
    return render(request, 'hello_word.html', {"title": "Contact us"})


def example_page(request):
    context = {'title': 'Example'}
    template_name = "hello_word.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))