from django.shortcuts import get_object_or_404, render

from constants import POSTS_NUMBER

from .models import Group, Post

# Create your views here.


def index(request):
    posts = Post.objects.all()[:POSTS_NUMBER]
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:POSTS_NUMBER]
    context = {
        "group": group,
        "posts": posts
    }
    return render(request, "posts/group_list.html", context)
