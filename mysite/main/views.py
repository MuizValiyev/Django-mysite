from django.shortcuts import get_object_or_404
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
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'main/posts/detail.html', {'post':post})