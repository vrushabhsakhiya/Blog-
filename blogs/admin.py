from django.contrib import admin
from django.urls import reverse
from .models import Blog, Category,  About_us, Follow, BlogLink, BlogPDF
from django.http import HttpResponseRedirect


# Inline resource links inside Blog
class BlogLinkInline(admin.TabularInline):
    model = BlogLink
    extra = 1
    verbose_name = "Website Link"
    verbose_name_plural = "Website Links"


# PDF inline
class BlogPDFInline(admin.TabularInline):
    model = BlogPDF
    extra = 1
    verbose_name = "PDF Download"
    verbose_name_plural = "PDF Downloads"

# Blog Admin
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status', 'created_at', 'is_featured')
    search_fields = ('id', 'title', 'status', 'category__category_name', 'author__username')
    list_editable = ('is_featured',)
    inlines = [BlogLinkInline, BlogPDFInline]


# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at')


# About Admin
@admin.register(About_us)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
     # allow only one About page
    def has_add_permission(self, request):
        if About_us.objects.exists():
            return False
        return True

    # after saving first record, go to edit page instead of add page
    def response_add(self, request, obj, post_url_continue=None):
        url = reverse("admin:blogs_about_us_change", args=[obj.id])  # noqa: F821
        return HttpResponseRedirect(url)


# Follow Admin
@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
