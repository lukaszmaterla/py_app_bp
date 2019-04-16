from django.shortcuts import render
from django.http import Http404
from .models import BlogPost


def blog_post_detail_page(request, id):
    try:
        obj = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
    template_name = 'blog_post_detail.html'
    context = {'obj': obj}
    return render(request, template_name, context)