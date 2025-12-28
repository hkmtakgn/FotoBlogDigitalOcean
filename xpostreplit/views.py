from django.shortcuts import render
from xpostreplit.models import Post
# Create your views here.


def home_views(request):
    posts = Post.objects.all()
    if posts is not None:
        posts = posts
    else:
        posts = None
    context = dict(posts=posts, )
    return render(request, "main/xpost-home.html", context)
