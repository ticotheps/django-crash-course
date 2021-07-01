from django.urls import path

from .views import todo_list, todo_read

app_name = "todos"

urlpatterns = [
    path('', todo_list),
    path('<id>/', todo_read)
]