from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all().order_by('-published_at')
    return render(request, 'blogs/blogs_list.html', {'blogs': blogs})

def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogs/blogs_details.html', {'blog': blog})
