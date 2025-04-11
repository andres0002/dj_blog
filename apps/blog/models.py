# django
from django.db import models
# third
from ckeditor.fields import RichTextField
# own


# Create your models here.

class Category(models.Model):
    nameCategory = models.CharField('Category Name', max_length=100, blank=False, null=False)
    conditionCategory = models.BooleanField('Category activa/deactivated', default=True)
    createDateCategory = models.DateTimeField('Createdate of Category', auto_now_add=True)
    updateDateCategory = models.DateTimeField('Update Date of Category', auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nameCategory

class Author(models.Model):
    nameAuthor = models.CharField('Name of Author', max_length=150, null=False, blank=False)
    lastNameAuthor = models.CharField('Lastname of Author', max_length=150, null=False, blank=False)
    facebookAuthor = models.URLField('Facebook of Author', null=True, blank=True)
    twitterAuthor = models.URLField('Twitter of Author', null=True, blank=True)
    instagram = models.URLField('Instagram of Author', null=True, blank=True)
    webAuthor = models.URLField('Web of Author', null=True, blank=True)
    emailAuthor = models.EmailField('Email of Author', null=False, blank=False)
    conditionAuthor = models.BooleanField('Author active/deactivated', default=True)
    createDateAuthor = models.DateTimeField('Createdate of Author', auto_now_add=True)
    updateDateAuthor = models.DateTimeField('Update Date of Author', auto_now=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.nameAuthor

class Post(models.Model):
    titlePost = models.CharField('Title of Post', max_length=100, null=False, blank=False)
    slugPost = models.CharField('Slug of Post', max_length=150, null=False, blank=False)
    descriptionPost = models.CharField('Description of Post', max_length=200, null=False, blank=False)
    contentsPost = RichTextField('Contents of Post')
    imagePost = models.URLField('URL of Image', max_length=300, null=False, blank=False)
    authorPost = models.ForeignKey(Author, on_delete=models.CASCADE)
    categoryPost = models.ForeignKey(Category, on_delete=models.CASCADE)
    conditionPost = models.BooleanField('Publicationed/Not Publicationed', default=True)
    createDatePost = models.DateTimeField('Createdate of Post', auto_now_add=True)
    updateDatePost = models.DateTimeField('Update Date of Post', auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        # Reemplazar espacios en slugPost por "_"
        if self.slugPost:
            self.slugPost = self.slugPost.strip().replace(' ', '_')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titlePost