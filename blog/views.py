from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from .forms import BlogPostForm, BlogPostModelForm
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
    obj = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        obj = (obj | my_qs).distinct()
    template_name = 'blog/list.html'
    context = {'object_list': obj}
    return render(request, template_name, context)


# @login_required()
@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        # obj.title = form.cleaned_data.get('title') + '-this is awesome'
        obj.user = request.user
        form.save()
        form = BlogPostModelForm()

    template_name = 'blog/form.html'
    context = {'form': form}
    return render(request, template_name, context)


@staff_member_required()
def blog_post_retrieve_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'obj': obj}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'title': f"Update {obj.title}", 'form': form}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.POST:
        obj.delete()
        redirect('/blog')
    context = {'obj': obj}
    return render(request, template_name, context)
