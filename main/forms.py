from django import forms 
from .models import Book, Article 
class BookForm(forms.ModelForm): 
    class Meta: 
        model = Book 
        fields = ['title', 'genre', 'page', 'status', 'like'] 

class ArticleForm(forms.ModelForm): 
    class Meta: 
        model = Article
        fields = ['title', 'subject', 'page', 'status', 'like'] 