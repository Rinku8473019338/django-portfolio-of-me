from django.shortcuts import render , get_object_or_404
from .models import Blog

def all_sites(request):
    blog_count = Blog.objects.count
    blogs = Blog.objects.order_by('-date')[:5]
    return render(request,'blog/all_sites.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog': blog})
