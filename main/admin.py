from django.contrib import admin
from .models import Book, Article, Subject, Genre

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done', 'genre', 'page')
    list_filter = ('genre',)
    search_fields = ('title',)
    
admin.site.register(Genre)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done', 'subject', 'page')
    list_filter = ('subject',)
    search_fields = ('title',)
    
admin.site.register(Subject)