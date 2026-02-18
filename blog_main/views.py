from django.shortcuts import render

from blogs.models import Blog, Category ,About_us, Follow
def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status='publish').order_by('created_at')
    posts= Blog.objects.filter(is_featured=False, status='publish')
    about_us = About_us.objects.all()
    follows = Follow.objects.all()
    context={
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about_us': about_us,
        'follows': follows,
        
    }
    return render(request, 'home.html', context)