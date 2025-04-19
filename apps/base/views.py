# django
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
# third
# own
from apps.blog.models import Post

# Create your views here.

def home_view(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(condition_post=True)
    if (queryset):
        posts = Post.objects.filter(
            Q(title_post__icontains=queryset) |
            Q(description_post__icontains=queryset),
            condition_post=True
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})