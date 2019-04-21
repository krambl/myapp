from django.shortcuts import render

def post_list(request):
    return render(request, 'myapp/main.html', {})

def webpay_list(request):
    return render(request, 'myapp/webpay.html', {})

