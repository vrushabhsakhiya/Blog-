from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.category_name
    
STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish')
)
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uplode/%y/%m/%d/')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class BlogLink(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="links"
    )

    url_heading = models.CharField(max_length=200)
    resource_link = models.URLField()

    def __str__(self):
        return self.url_heading
class BlogPDF(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="pdfs"
    )

    pdf_title = models.CharField(max_length=200)

    pdf_file = models.FileField(
        upload_to='blog_pdfs/',
        validators=[FileExtensionValidator(['pdf'])]  # only pdf allowed
    )

    def __str__(self):
        return self.pdf_title



class About_us(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'About Us'
    
    def __str__(self):
        return self.title
    
class Follow(models.Model):
    ICON_CHOICES = (
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('x', 'x'),
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('email', 'Email'),
        ('website', 'Website'),
    )

    name = models.CharField(max_length=50, choices=ICON_CHOICES)
    url = models.URLField()

    def __str__(self):
        return self.name
