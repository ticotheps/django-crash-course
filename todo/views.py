from django.http import HttpResponse
from django.shortcuts import render


def todo_list(request):
    return HttpResponse("Hello World")
