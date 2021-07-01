from django.urls import path

from .views import todo_list, todo_create, todo_read

app_name = "todos"

urlpatterns = [
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_read)
]