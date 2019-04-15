from django.http import HttpResponse


def home_page(request):
    return HttpResponse('<h1>Hello Word</h1')


def about(request):
    return HttpResponse('<h1>About us</h1')


def contact(request):
    return HttpResponse('<h1>Contact us</h1')
