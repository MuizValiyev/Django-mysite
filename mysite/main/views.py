from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    post = Post.published.all()
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

    context = {
        'posts':posts
    }
    return render(request, 'main/posts/list.html', context)


def post_detail(request, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)
    return render(request, 'main/posts/detail.html', {'post':post})