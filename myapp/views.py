from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.all

    return render(request, 'myapp/main.html', {'posts': posts})

def webpay_list(request):
    post = Post.objects.get(title="Webpay")
    return render(request, 'myapp/webpay.html', {post})

