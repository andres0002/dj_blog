# django
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
# third
# own
from apps.blog.models import Post, Category

# Create your views here.

def home(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(conditionPost=True)
    if (queryset):
        posts = Post.objects.filter(
            Q(titlePost__icontains=queryset) |
            Q(descriptionPost__icontains=queryset),
            conditionPost=True
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})

def generals(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(
        conditionPost = True,
        categoryPost = Category.objects.get(nameCategory__iexact='General')
    )
    if (queryset):
        posts = Post.objects.filter(
            Q(titlePost__icontains=queryset) |
            Q(descriptionPost__icontains=queryset),
            conditionPost = True,
            categoryPost = Category.objects.get(nameCategory__iexact='General')
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'generals.html', {'posts': posts})

def programation(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(
        conditionPost = True,
        categoryPost = Category.objects.get(nameCategory__iexact='Programation')
    )
    if (queryset):
        posts = Post.objects.filter(
            Q(titlePost__icontains=queryset) |
            Q(descriptionPost__icontains=queryset),
            conditionPost=True,
            categoryPost = Category.objects.get(nameCategory__iexact='Programation')
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'programation.html', {'posts': posts})

def video_games(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(
        conditionPost = True,
        categoryPost = Category.objects.get(nameCategory__iexact='VideoGames')
    )
    if (queryset):
        posts = Post.objects.filter(
            Q(titlePost__icontains=queryset) |
            Q(descriptionPost__icontains=queryset),
            conditionPost=True,
            categoryPost = Category.objects.get(nameCategory__iexact='VideoGames')
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'videogames.html', {'posts': posts})

def tecnology(request):
    queryset = request.GET.get('search')
    posts = Post.objects.filter(
        conditionPost = True,
        categoryPost = Category.objects.get(nameCategory__iexact='Tecnologies')
    )
    if (queryset):
        posts = Post.objects.filter(
            Q(titlePost__icontains=queryset) |
            Q(descriptionPost__icontains=queryset),
            conditionPost=True,
            categoryPost = Category.objects.get(nameCategory__iexact='Tecnologies')
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'tecnology.html', {'posts': posts})

def detail_post(request, slug):
    post = get_object_or_404(Post, slugPost=slug)
    return render(request, 'post.html', {'post': post})