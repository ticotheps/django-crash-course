from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    return render(request, "todo_list.html")