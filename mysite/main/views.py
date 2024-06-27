from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmilPostForm


def post_list(request):
    post = Post.published.all()
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page', 1)
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(1)
    context = {
        'posts':posts
    }
    return render(request, 'main/posts/list.html', context)


def post_detail(request, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)
    return render(request, 'main/posts/detail.html', {'post':post})

def oist_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmilPostForm(request.POST)
        if form.if_valid():
            cd = form.cleaned_data
    else:
        form = EmilPostForm()
    return render(request, 'main/posts/share.html', {'post':post, 'form':form})