from django.shortcuts import render


def search_view(request):
    context = {}
    return render(request, 'searches/view.html', context)
