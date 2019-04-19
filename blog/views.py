from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .forms import BlogPostForm
from .models import BlogPost


def blog_post_detail_view(request, slug):
    # queryset = BlogPost.objects.filter(slug=slug)
    # if queryset.count() == 0:
    #     raise Http404
    # obj = queryset.first()
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'obj': obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    obj = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {'object_list': obj}
    return render(request, template_name, context)


def blog_post_create_view(request):
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        obj = BlogPost.objects.create(**form.cleaned_data)
        form = BlogPostForm()
    template_name = 'blog/form.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_retrieve_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'obj': obj}
    return render(request, template_name, context)


def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {'obj': obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {'obj': obj}
    return render(request, template_name, context)
