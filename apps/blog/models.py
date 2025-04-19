# django
from django.db import models
from django.core.exceptions import ValidationError
# third
from ckeditor.fields import RichTextField
# own

# Create your models here.

class Category(models.Model):
    name_category = models.CharField('Category Name', max_length=100, blank=False, null=False, unique=True)
    condition_category = models.BooleanField('Category active/deactivated', default=True)
    create_date_category = models.DateTimeField('Create Date of Category', auto_now_add=True)
    update_date_category = models.DateTimeField('Update Date of Category', auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def clean(self):
        super().clean()
        # Buscar si ya existe otra categoría con el mismo nombre, sin importar mayúsculas o minusculas.
        if Category.objects.filter(name_category__iexact=self.name_category).exclude(id=self.id).exists():
            raise ValidationError({
                'name_category': "Ya existe una categoría con ese nombre (sin importar mayúsculas, minúsculas y espacios al inicio o al final)."
            })
    
    def seve(self, *args, **kwargs):
        self.name_category = self.name_category.strip() # normaliza el valor -> quita espacios al inicio y al final.
        self.full_clean() # Ejecuta clean() antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_category

class Author(models.Model):
    name_author = models.CharField('Name of Author', max_length=150, null=False, blank=False)
    lastname_author = models.CharField('Lastname of Author', max_length=150, null=False, blank=False)
    facebook_author = models.URLField('Facebook of Author', null=True, blank=True)
    twitter_author = models.URLField('Twitter of Author', null=True, blank=True)
    instagram_author = models.URLField('Instagram of Author', null=True, blank=True)
    web_author = models.URLField('Web of Author', null=True, blank=True)
    email_author = models.EmailField('Email of Author', null=False, blank=False, unique=True)
    condition_author = models.BooleanField('Author active/deactivated', default=True)
    create_date_author = models.DateTimeField('Create Date of Author', auto_now_add=True)
    update_date_author = models.DateTimeField('Update Date of Author', auto_now=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        unique_together = ('name_author', 'lastname_author')  # para que al author sea unico

    def __str__(self):
        return f'{self.lastname_author} {self.name_author}'

class Post(models.Model):
    title_post = models.CharField('Title of Post', max_length=100, null=False, blank=False, unique=True)
    slug_post = models.CharField('Slug of Post', max_length=150, null=False, blank=False, unique=True)
    description_post = models.CharField('Description of Post', max_length=200, null=False, blank=False)
    contents_post = RichTextField('Contents of Post')
    image_post = models.URLField('URL of Image', max_length=300, null=False, blank=False)
    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_post = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition_post = models.BooleanField('Publicationed/Not Publicationed', default=True)
    create_date_post = models.DateTimeField('Create Date of Post', auto_now_add=True)
    update_date_post = models.DateTimeField('Update Date of Post', auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        # Reemplazar espacios en slug_post por "_"
        if self.slug_post:
            self.slug_post = self.slug_post.strip().replace(' ', '_')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_post