# django
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# third
# own
from apps.blog.models import Category, Author, Post

# Register your models here.

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nameCategory']
    readonly_fields = ('createDateCategory', 'updateDateCategory')
    list_display = ('nameCategory', 'conditionCategory', 'createDateCategory', 'updateDateCategory')
    list_filter = ('conditionCategory', 'createDateCategory', 'updateDateCategory')
    ordering = ['nameCategory']
    resource_class = CategoryResource

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nameAuthor', 'lastNameAuthor', 'emailAuthor']
    readonly_fields = ('createDateAuthor', 'updateDateAuthor')
    list_display = ('nameAuthor', 'lastNameAuthor', 'facebookAuthor', 'twitterAuthor', 'instagram', 'webAuthor', 'emailAuthor', 'conditionAuthor', 'createDateAuthor', 'updateDateAuthor')
    list_filter = ('conditionAuthor', 'createDateAuthor', 'updateDateAuthor')
    ordering = ['nameAuthor']
    resource_class = AuthorResource

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titlePost', 'slugPost', 'descriptionPost', 'authorPost', 'categoryPost', 'createDatePost', 'updateDatePost']
    readonly_fields = ('createDatePost', 'updateDatePost')
    list_display = ('titlePost', 'slugPost', 'descriptionPost', 'authorPost', 'categoryPost', 'conditionPost', 'createDatePost', 'updateDatePost')
    list_filter = ('authorPost', 'categoryPost', 'conditionPost', 'createDatePost', 'updateDatePost')
    ordering = ['titlePost']
    resource_class = PostResource

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)