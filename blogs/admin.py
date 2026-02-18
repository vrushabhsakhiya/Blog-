from django.contrib import admin
from .models import Blog, Category
# Register your models here.
#slug automatically generate from title
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status',  'created_at','is_featured',)
    search_fields = ('id', 'title', 'status','category__category_name', 'author__username')
    list_editable = ( 'is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)