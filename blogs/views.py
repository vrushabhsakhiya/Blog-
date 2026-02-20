from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.db.models import Q
from .models import Follow, Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category=category_id, status='publish')
    try:
        category = Category.objects.get(pk=category_id)  
    except:  
        return render(request, '404.html', status=404) 
    # catogry = get_object_or_404(Category, pk=category_id)
    context ={
        'posts': posts,
        'category': category,
    }
    
    return render(request,'posts_by_category.html', context)

#for this function single blog post will be shown when we click on the blog title in home page
def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='publish')
    categories = Category.objects.all()
    follows = Follow.objects.all()
    
    # ⭐ RELATED BLOGS (same category)
    related_blogs = Blog.objects.filter(
        category=single_blog.category,
        status='publish'
    ).exclude(id=single_blog.id)[:4]
    context = {
        'single_blog': single_blog,
        'categories': categories,
        'follows': follows,
        'related_blogs': related_blogs, 
    }   
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')

    blogs = []

    if keyword:   # ⭐ only search when user types something
        blogs = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword) |
            Q(blog_body__icontains=keyword),
            status='publish'
        )

    context = {
        'blogs': blogs,
        'keyword': keyword,   # ⭐ THIS WAS MISSING
    }

    return render(request, 'search.html', context)
