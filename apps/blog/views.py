# django
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# third
# own
from apps.blog.models import Post, Category

# Create your views here.

def generals_view(request):
    queryset = request.GET.get('search')
    categoty_post = Category.objects.filter(name_category__iexact='General').first()
    if not categoty_post:
        categoty_post = Category.objects.create(name_category='General')
    posts = Post.objects.filter(
        condition_post = True,
        category_post = categoty_post
    )
    if (queryset):
        posts = Post.objects.filter(
            Q(title_post__icontains=queryset) |
            Q(description_post__icontains=queryset),
            condition_post = True,
            category_post = categoty_post
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'generals.html', {'posts': posts})

def programation_view(request):
    queryset = request.GET.get('search')
    category_post = Category.objects.filter(name_category__iexact='Programation').first()
    if not category_post:
        category_post = Category.objects.create(name_category='Programation')
    posts = Post.objects.filter(
        condition_post = True,
        category_post = category_post
    )
    if (queryset):
        posts = Post.objects.filter(
            Q(title_post__icontains=queryset) |
            Q(description_post__icontains=queryset),
            condition_post=True,
            category_post = category_post
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'programation.html', {'posts': posts})

def video_games_view(request):
    queryset = request.GET.get('search')
    category_post = Category.objects.filter(name_category__iexact='VideoGames').first()
    if not category_post:
        category_post = Category.objects.create(name_category='VideoGames')
    posts = Post.objects.filter(
        condition_post = True,
        category_post = category_post
    )
    if (queryset):
        posts = Post.objects.filter(
            Q(title_post__icontains=queryset) |
            Q(description_post__icontains=queryset),
            condition_post=True,
            category_post = category_post
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'videogames.html', {'posts': posts})

def tecnology_view(request):
    queryset = request.GET.get('search')
    category_post = Category.objects.filter(name_category__iexact='Tecnology').first()
    if not category_post:
        category_post = Category.objects.create(name_category='Tecnology')
    posts = Post.objects.filter(
        condition_post = True,
        category_post = category_post
    )
    if (queryset):
        posts = Post.objects.filter(
            Q(title_post__icontains=queryset) |
            Q(description_post__icontains=queryset),
            condition_post=True,
            category_post = category_post
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tecnology.html', {'posts': posts})

def detail_post_view(request, slug):
    post = get_object_or_404(Post, slug_post=slug)
    return render(request, 'post.html', {'post': post})