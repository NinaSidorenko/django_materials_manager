from django.urls import path 
from . import views 
urlpatterns = [ 
path('', views.books_articles_list, name="books_articles_list"), 
path('bookcreate/', views.book_create, name="book_create"),
path('articlecreate/', views.article_create, name="article_create"), 
path('bookupdate/<int:pk>/', views.book_update, name="book_update"), 
path('articleupdate/<int:pk>/', views.article_update, name="article_update"), 
path('bookdelete/<int:pk>/', views.book_delete, name="book_delete"), 
path('articledelete/<int:pk>/', views.article_delete, name="article_delete"), 
] 