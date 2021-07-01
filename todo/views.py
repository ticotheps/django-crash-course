from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo

# The LIST view - Generates a full list of every todo item.
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    context = {
        "todo_list": todos
    }
    return render(request, "todo_list.html", context)

# The READ view - Retrieves any todo item based on the todo's id.
def todo_read(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo_read.html", context)