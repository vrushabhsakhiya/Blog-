from django.shortcuts import render

from blogs.models import Blog,About_us, Follow
def home(request):
    
    featured_posts = Blog.objects.filter(is_featured=True,status='publish').order_by('created_at')
    posts= Blog.objects.filter(is_featured=False, status='publish')
    about_us = About_us.objects.all()
    follows = Follow.objects.all()
    context={
        'featured_posts': featured_posts,
        'posts': posts,
        'about_us': about_us,
        'follows': follows,
        
    }
    return render(request, 'home.html', context)

