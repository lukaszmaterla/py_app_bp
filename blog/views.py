from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost


def blog_post_detail_page(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() >= 1:
        obj = queryset.first()

    # obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {'obj': obj}
    return render(request, template_name, context)