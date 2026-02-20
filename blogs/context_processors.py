from blogs.models import Blog, Category, Follow

def get_categories(request):
    categories = Category.objects.all()
    follows = Follow.objects.all()
    resourse_link = Blog.objects.filter(is_featured=True, status='publish').order_by('created_at')
    return dict(categories=categories, follows=follows, resourse_link=resourse_link)