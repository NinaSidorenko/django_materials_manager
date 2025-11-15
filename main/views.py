from django.shortcuts import render
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Привет, это мой первый Django-проект!")


from .models import Task
def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks_list.html", {"tasks": tasks})