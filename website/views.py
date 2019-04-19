from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm

def home_page(request):
    my_title = 'hello there...'
    return render(request, 'home.html', {"title": my_title})


def about(request):
    return render(request, 'about.html', {"title": "About us"})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        "title": "Contact us",
        'form': form
    }
    return render(request, 'form.html', context)


def example_page(request):
    context = {'title': 'Example'}
    template_name = "hello_word.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))