from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo

# generates full list of all todo items
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    context = {
        "todo_list": todos
    }
    return render(request, "todo_list.html", context)

# Read any todo item based on id
def todo_read(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo_read.html", context)