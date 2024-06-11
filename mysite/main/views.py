from django.shortcuts import render
from django.http import Http404
from .models import Post



def post_list(request):
    posts = Post.published.all()
    context = {
        'posts':posts
    }
    return render(request, 'main/posts/list.html', context)


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No Post found.')
    return render(request, 'main/posts/detail.html', {'post':post})