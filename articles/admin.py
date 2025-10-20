from django.contrib import admin
from .models import Article,Comment
# Register your models here.

class CommentInline(admin.TabularInline): 
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        ]
    List_display = ['title', 'author', 'body',]


admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment) 
