# django
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
# third
# own
from apps.blog.models import Post, Category

# Create your views here.

def home_view(request):
    search = request.GET.get('search')
    posts = Post.objects.filter(condition_post=True)
    if search:
        posts = posts.filter(
            Q(title_post__icontains=search) |
            Q(description_post__icontains=search)
        ).distinct() # distinct() -> elimina duplicados
    # Paginator.
    paginator = Paginator(posts, 2)
    # Get page current.
    page = request.GET.get('page')
    # Posts estructurados por page.
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    # context_object_name = 'posts' # como lista
    paginate_by = 2

    def get_queryset(self):
        search = self.request.GET.get('search')
        posts = self.model.objects.filter(condition_post=True)
        if search:
            posts = posts.filter(
                Q(title_post__icontains=search) |
                Q(description_post__icontains=search)
            ).distinct() # distinct() -> elimina duplicados
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['page_obj']  # Para utilizar posts (como paginator) en tamplate.
        context['request'] = self.request # Para utilizar request en tamplate.
        return context

def generals_view(request):
    search = request.GET.get('search')
    categoty_post = Category.objects.filter(name_category__iexact='General').first()
    if not categoty_post:
        categoty_post = Category.objects.create(name_category='General')
    posts = Post.objects.filter(
        condition_post = True,
        category_post = categoty_post
    )
    if search:
        posts = posts.filter(
            Q(title_post__icontains=search) |
            Q(description_post__icontains=search)
        ).distinct() # distinct() -> elimina duplicados
    # Paginator.
    paginator = Paginator(posts, 2)
    # Get page current.
    page = request.GET.get('page')
    # Posts estructurados por page.
    posts = paginator.get_page(page)
    return render(request, 'generals.html', {'posts': posts})

class GeneralsView(ListView):
    model = Post
    template_name = 'generals.html'
    # context_object_name = 'posts' # como lista
    paginate_by = 2

    def get_queryset(self):
        search = self.request.GET.get('search')
        
        # Obtener o crear la categoría 'General'
        category_post = Category.objects.filter(name_category__iexact='General').first()
        if not category_post:
            category_post = Category.objects.create(name_category='General')
        
        # Filtrar los posts por categoría y condición
        posts = Post.objects.filter(
            condition_post=True,
            category_post=category_post
        )

        # Si hay búsqueda, aplicar el filtro adicional
        if search:
            posts = posts.filter(
                Q(title_post__icontains=search) |
                Q(description_post__icontains=search)
            ).distinct() # distinct() -> elimina duplicados
        
        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['page_obj']  # Para utilizar posts (como paginator) en tamplate.
        context['request'] = self.request # Para utilizar request en tamplate.
        return context

def programation_view(request):
    search = request.GET.get('search')
    category_post = Category.objects.filter(name_category__iexact='Programation').first()
    if not category_post:
        category_post = Category.objects.create(name_category='Programation')
    posts = Post.objects.filter(
        condition_post = True,
        category_post = category_post
    )
    if search:
        posts = posts.filter(
            Q(title_post__icontains=search) |
            Q(description_post__icontains=search)
        ).distinct() # distinct() -> elimina duplicados
    # Paginator.
    paginator = Paginator(posts, 2)
    # Get page current.
    page = request.GET.get('page')
    # Posts estructurados por page.
    posts = paginator.get_page(page)
    return render(request, 'programation.html', {'posts': posts})

class ProgramationView(ListView):
    model = Post
    template_name = 'programation.html'
    # context_object_name = 'posts' # como lista
    paginate_by = 2

    def get_queryset(self):
        search = self.request.GET.get('search')

        # Obtener o crear la categoría 'Programation'
        category_post = Category.objects.filter(name_category__iexact='Programation').first()
        if not category_post:
            category_post = Category.objects.create(name_category='Programation')

        # Obtener posts filtrados por categoría y condición activa
        posts = Post.objects.filter(
            condition_post=True,
            category_post=category_post
        )

        # Si hay búsqueda, aplicar filtro
        if search:
            posts = posts.filter(
                Q(title_post__icontains=search) |
                Q(description_post__icontains=search)
            ).distinct() # distinct() -> elimina duplicados

        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['page_obj']  # Para utilizar posts (como paginator) en tamplate.
        context['request'] = self.request # Para utilizar request en tamplate.
        return context

def video_games_view(request):
    search = request.GET.get('search')
    category_post = Category.objects.filter(name_category__iexact='VideoGames').first()
    if not category_post:
        category_post = Category.objects.create(name_category='VideoGames')
    posts = Post.objects.filter(
        condition_post = True,
        category_post = category_post
    )
    if search:
        posts = posts.filter(
            Q(title_post__icontains=search) |
            Q(description_post__icontains=search)
        ).distinct() # distinct() -> elimina duplicados
    # Paginator.
    paginator = Paginator(posts, 2)
    # Get page current.
    page = request.GET.get('page')
    # Posts estructurados por page.
    posts = paginator.get_page(page)
    return render(request, 'videogames.html', {'posts': posts})

class VideoGamesView(ListView):
    model = Post
    template_name = 'videogames.html'
    # context_object_name = 'posts' # como lista
    paginate_by = 2

    def get_queryset(self):
        search = self.request.GET.get('search')

        # Obtener o crear la categoría 'VideoGames'
        category_post = Category.objects.filter(name_category__iexact='VideoGames').first()
        if not category_post:
            category_post = Category.objects.create(name_category='VideoGames')

        # Filtrar posts activos de la categoría
        posts = Post.objects.filter(
            condition_post=True,
            category_post=category_post
        )

        # Si hay búsqueda, aplicar filtro extra
        if search:
            posts = posts.filter(
                Q(title_post__icontains=search) |
                Q(description_post__icontains=search)
            ).distinct() # distinct() -> elimina duplicados

        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['page_obj']  # Para utilizar posts (como paginator) en tamplate.
        context['request'] = self.request # Para utilizar request en tamplate.
        return context

def tecnology_view(request):
    search = request.GET.get('search')
    category_post = Category.objects.filter(name_category__iexact='Tecnology').first()
    if not category_post:
        category_post = Category.objects.create(name_category='Tecnology')
    posts = Post.objects.filter(
        condition_post = True,
        category_post = category_post
    )
    if search:
        posts = posts.filter(
            Q(title_post__icontains=search) |
            Q(description_post__icontains=search)
        ).distinct() # distinct() -> elimina duplicados
    # Paginator.
    paginator = Paginator(posts, 2)
    # Get page current.
    page = request.GET.get('page')
    # Posts estructurados por page.
    posts = paginator.get_page(page)
    return render(request, 'tecnology.html', {'posts': posts})

class TecnologyView(ListView):
    model = Post
    template_name = 'tecnology.html'
    # context_object_name = 'posts' # como lista
    paginate_by = 2

    def get_queryset(self):
        search = self.request.GET.get('search')

        # Obtener o crear la categoría 'Tecnology'
        category_post = Category.objects.filter(name_category__iexact='Tecnology').first()
        if not category_post:
            category_post = Category.objects.create(name_category='Tecnology')

        # Filtrar posts activos de la categoría
        posts = Post.objects.filter(
            condition_post=True,
            category_post=category_post
        )

        # Si hay búsqueda, aplicar filtro extra
        if search:
            posts = posts.filter(
                Q(title_post__icontains=search) |
                Q(description_post__icontains=search)
            ).distinct() # distinct() -> elimina duplicados

        return posts
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['page_obj']  # Para utilizar posts (como paginator) en tamplate.
        context['request'] = self.request # Para utilizar request en tamplate.
        return context

def detail_post_view(request, slug):
    post = get_object_or_404(Post, slug_post=slug)
    return render(request, 'post.html', {'post': post})

class DetailPostView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    slug_field = 'slug_post'
    slug_url_kwarg = 'slug'