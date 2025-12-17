from django.shortcuts import render, redirect, get_object_or_404 
from .models import Book, Article, Subject, Genre
from .forms import BookForm, ArticleForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Book, Article
def books_articles_list(request):
    books = Book.objects.all()
    articles = Article.objects.all()

    genre = request.GET.get('genre')
    status_b = request.GET.get('status')
    query_b = request.GET.get('q_b')

    if genre:
        books = books.filter(genre__id=genre)
    if status_b == 'Прочитана':
        books = books.filter(is_done=True)
    if query_b:
        books = books.filter(title__icontains=query_b)
    elif status_b == 'В процессе':
        books = books.filter(is_done=False)

    paginator = Paginator(books, 5) # 5 задач на страницу
    page = request.GET.get('page')
    books = paginator.get_page(page)

    return render(request, "books_articles_list.html", {
        "books": books,
        "articles": articles,
        "genres": Genre.objects.all(),
        "subjects": Subject.objects.all(),
    })



@login_required
def book_create(request): 
        if request.method == "POST": 
            form = BookForm(request.POST) 
            if form.is_valid(): 
                task = form.save(commit=False)
                task.save() 
                return redirect('books_articles_list') 
        else: 
            form = BookForm() 
        return render(request, "book_form.html", {"form": form}) 

@login_required
def article_create(request): 
        if request.method == "POST": 
            form = ArticleForm(request.POST) 
            if form.is_valid(): 
                task = form.save(commit=False)
                task.save() 
                return redirect('books_articles_list') 
        else: 
            form = BookForm() 
        return render(request, "article_form.html", {"form": form}) 

@login_required
def book_update(request, pk): 
    task = get_object_or_404(Book, pk=pk) 
    if request.method == "POST": 
        form = BookForm(request.POST, instance=task) 
        if form.is_valid(): 
            book = form.save(commit=False) # проверить, нужно ли это и следующая строка, если получится странно - убрать
            form.save() 
            return redirect('books_articles_list') 
    else: 

        form = BookForm(instance=task) 
    return render(request, "book_form.html", {"form": form})

@login_required
def article_update(request, pk): 
    task = get_object_or_404(Book, pk=pk) 
    if request.method == "POST": 
        form = ArticleForm(request.POST, instance=task) 
        if form.is_valid(): 
            article = form.save(commit=False) # проверить, нужно ли это и следующая строка, если получится странно - убрать
            form.save() 
            return redirect('books_articles_list') 
    else: 

        form = ArticleForm(instance=task) 
    return render(request, "article_form.html", {"form": form})

@login_required
def book_delete(request, pk): 
    book = get_object_or_404(Book, pk=pk) 
    if request.method == "POST": 
        book.delete() 
        return redirect('books_articles_list') 
    return render(request, "book_confirm_delete.html", {"book": book}) 

@login_required
def article_delete(request, pk): 
    article = get_object_or_404(Book, pk=pk) 
    if request.method == "POST": 
        article.delete() 
        return redirect('books_articles_list') 
    return render(request, "article_confirm_delete.html", {"article": article}) 