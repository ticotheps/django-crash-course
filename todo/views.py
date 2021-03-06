from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm  

# LIST view - generates a full list of every todo object.
def todo_list(request):
    todos = Todo.objects.all()
    print(todos)
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_list.html", context)


# CREATE view - allows creation of a new todo object via a form.
def todo_create(request):
    # pass data into the 'TodoForm' only if this is a POST request.
    form = TodoForm(request.POST or None)
    # Use Django's 'forms' module to validate the data passed into the form.
    if form.is_valid():
        # # print(form.cleaned_data)
        # name = form.cleaned_data['name']
        # due_date = form.cleaned_data['due_date']
        # print(name, due_date)
        
        # # create a new todo object
        # new_todo = Todo.objects.create(name=name, due_date=due_date)
        
        form.save()
        # redirect the user back to the todo list
        return redirect("/")
    context = {
        "form": form
    }
    return render(request, "todo/todo_create.html", context)


# READ view - retrieves any todo item based on the todo's id.
def todo_read(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_read.html", context)


# UPDATE view - updates any todo item based on the todo's id.
def todo_update(request, id):
    # retrieve a todo object by id.
    todo = Todo.objects.get(id=id)
    # pass data into the 'TodoForm' only if this is a POST request.
    form = TodoForm(request.POST or None, instance=todo)
    # Use Django's 'forms' module to validate the data passed into the form.
    if form.is_valid():
        form.save()
        # redirect the user back to the todo list
        return redirect("/")
    context = {
        "form": form
    }
    return render(request, "todo/todo_update.html", context)


# DELETE view - removes any todo item based on the todo's id.
def todo_delete(request, id):
    # todo = Todo.objects.filter(id=id).delete()
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect("/")