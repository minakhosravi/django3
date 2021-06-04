from .models import shop
from django.shortcuts import render, get_object_or_404

def shop_list(request):
    posts_all = shop.objects.all()
    return render(request,'shop/post/index.html',{'posts': posts_all})

