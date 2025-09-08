from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Васин В.С.</i>
    """
    return HttpResponse(text)
