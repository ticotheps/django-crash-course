from django.urls import path

from .views import (
    todo_list,
    todo_create,
    todo_read,
    todo_update
)

app_name = "todos"

urlpatterns = [
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_read),
    path('<id>/update', todo_update)
]