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
    search_fields = ['name_category']
    readonly_fields = ('create_date_category', 'update_date_category')
    list_display = ('name_category', 'condition_category', 'create_date_category', 'update_date_category')
    list_filter = ('condition_category', 'create_date_category', 'update_date_category')
    ordering = ['name_category']
    resource_class = CategoryResource

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name_author', 'lastname_author', 'email_author']
    readonly_fields = ('create_date_author', 'update_date_author')
    list_display = ('name_author', 'lastname_author', 'facebook_author', 'twitter_author', 'instagram_author', 'web_author', 'email_author', 'condition_author', 'create_date_author', 'update_date_author')
    list_filter = ('condition_author', 'create_date_author', 'update_date_author')
    ordering = ['name_author']
    resource_class = AuthorResource

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title_post', 'slug_post', 'description_post', 'author_post', 'category_post', 'create_date_post', 'update_date_post']
    readonly_fields = ('create_date_post', 'update_date_post')
    list_display = ('title_post', 'slug_post', 'description_post', 'author_post', 'category_post', 'condition_post', 'create_date_post', 'update_date_post')
    list_filter = ('author_post', 'category_post', 'condition_post', 'create_date_post', 'update_date_post')
    ordering = ['title_post']
    resource_class = PostResource

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)