from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmilPostForm
from django.core.mail import send_mail


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

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    sent = False

    if request.method == 'POST':
        form = EmilPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri( post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n {cd['name']}\'s comments: {cd['comment']}"
            send_mail(subject, message, 'valiyevmuiz0407@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmilPostForm()
    return render(request, 'main/posts/share.html', {'post': post, 'form': form, 'sent': sent})
